from django.contrib import admin
from .models import Order, RoomType, UserProfile


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'count', 'price',)#要显示的字段名


class OrderAdmin(admin.ModelAdmin):
    list_display = ('type', 'count', 'customer', 'begin_time', 'end_time')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name')

admin.site.register(Order, OrderAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(UserProfile, UserAdmin)
