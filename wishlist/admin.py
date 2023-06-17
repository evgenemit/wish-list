from django.contrib import admin

from .models import Wish, WishList


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'is_busy')
    list_editable = ('is_busy', )


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
