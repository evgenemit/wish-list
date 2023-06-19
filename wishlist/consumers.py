import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from api.services import wish_services, wishlist_services
from api.base_api import ERROR


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
        """
        Обрабатывает событие бронирования, разбронирования
        чтения спика желаний и длбавление, удаление желания
        """
        text_data_json = json.loads(text_data)
        # id желания
        wish_id = text_data_json.get('wish_id', None)
        # тип действия
        code = text_data_json.get('code', None)
        res = ERROR.copy()

        is_error = True
        if code == 'book':
            # посылка сообщения всем участникам группы
            res = wish_services.book_wish(wish_id)
            if res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name,
                    {
                        'type': 'wish_book_unbook',
                        'wish_id': wish_id,
                        'is_busy': True
                    }
                )
        elif code == 'unbook':
            res = wish_services.unbook_wish(wish_id)
            if res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name,
                    {
                        'type': 'wish_book_unbook',
                        'wish_id': wish_id,
                        'is_busy': False
                    }
                )
        elif code == 'all_wishes':
            # получение списка всех желаний
            user_id = text_data_json.get('user_id', None)
            res = wishlist_services.get_whislist(user_id)
            if res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name,
                    {
                        'type': 'get_wishlist',
                        'wishes': res['wishlist']['wishes']
                    }
                )
        elif code == 'add_wish':
            wishlist_id = text_data_json.get('wishlist_id', None)
            w_text = text_data_json.get('text', None)
            w_about = text_data_json.get('about', None)
            w_link = text_data_json.get('link', None)
            res = wish_services.create_wish(
                wishlist_id, w_text, w_about, w_link
            )
            if res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name,
                    {
                        'type': 'add_wish',
                        'wish': res['wish']
                    }
                )
        elif code == 'delete_wish':
            wish_id = text_data_json.get('wish_id', None)
            res = wish_services.delete_wish(wish_id)
            if res['status'] == 'ok':
                is_error = False
                async_to_sync(self.channel_layer.group_send)(
                    self.wishlist_group_name,
                    {
                        'type': 'delete_wish',
                        'wish_id': wish_id
                    }
                )

        # если произошла ошибка, возвращаем текст
        if is_error:
            if code is None:
                res['message'] = 'Не передан параметр code.'
            self.send(text_data=json.dumps(res))

    def wish_book_unbook(self, event):
        wish_id = event['wish_id']
        is_busy = event['is_busy']

        self.send(text_data=json.dumps(
            {'code': 'book_unbook', 'wish_id': wish_id, 'is_busy': is_busy}
        ))

    def get_wishlist(self, event):
        wishes = event['wishes']

        self.send(text_data=json.dumps({'code': 'wishlist', 'wishes': wishes}))

    def add_wish(self, event):
        wish = event['wish']

        self.send(text_data=json.dumps({'code': 'add_wish', 'wish': wish}))

    def delete_wish(self, event):
        wish_id = event['wish_id']

        self.send(text_data=json.dumps(
            {'code': 'delete_wish', 'wish_id': wish_id}
        ))
