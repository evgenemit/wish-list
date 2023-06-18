import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from api.services import wish_services


class WishlistConsumer(WebsocketConsumer):
    """Обрабатывает соединения, связанные с бронированием желаний в списке"""

    def connect(self):
        """Устанавливает соединение"""
        self.wishlist_name = self.scope['url_route']['kwargs']['wishlist_name']
        self.wishlist_group_name = f'wishlist_{self.wishlist_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.wishlist_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """Завершает соединение"""
        async_to_sync(self.channel_layer.group_discard)(
            self.wishlist_group_name, self.channel_name
        )

    def receive(self, text_data):
        """Обрабатывает событие бронирования и разбронирования"""
        text_data_json = json.loads(text_data)
        # id желания
        wish_id = text_data_json['wish_id']
        # тип действия
        code = text_data_json['code']

        is_error = True
        if code == 'book':
            # посылка сообщения всем участникам группы
            wish_res = wish_services.book_wish(wish_id)
            if wish_res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name, {'type': 'wish_book_unbook', 'wish_id': wish_id, 'is_busy': True}
                )
        elif code == 'unbook':
            wish_res = wish_services.unbook_wish(wish_id)
            if wish_res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name, {'type': 'wish_book_unbook', 'wish_id': wish_id, 'is_busy': False}
                )
        
        # если произошла ошибка, возвращаем текст
        if is_error:
            self.send(text_data=json.dumps(wish_res))


    def wish_book_unbook(self, event):
        wish_id = event['wish_id']
        is_busy = event['is_busy']

        self.send(text_data=json.dumps({'wish_id': wish_id, 'is_busy': is_busy}))
