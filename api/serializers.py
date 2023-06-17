from rest_framework.serializers import ModelSerializer

from wishlist.models import Wish, WishList


class WishListSerializer(ModelSerializer):
    """Все данные о списке желаний"""

    class Meta:
        model = WishList
        fields = '__all__'


class WishSerializer(ModelSerializer):
    """Все данные о желании"""

    class Meta:
        model = Wish
        exclude = ('wishlist', )
