from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UsersAdmin(UserAdmin):
    """
    Управление пользователями в админ панели.
    Доступные функции администратору:
    1- изменение пароля пользователя;
    2- изменение профиля пользователя;
    3- поиск по имени и почте;
    4- фильтр по почте и фамилии;
    5- блокировка пользователя;
    6- удаление аккаунтов.
    Обратите внимание!
    Логин и адрес электронной почты не чувствительны к регистру.
    """
    list_display = ('username', 'email',
                    'first_name', 'last_name', 'role')
    fieldsets = (("User",
                 {"fields": (
                     'username', 'password', 'email',
                     'first_name', 'last_name',
                     'role', 'last_login', 'date_joined')}),)
    search_fields = ('first_name', 'email',)
    list_filter = ('email', 'first_name',)


admin.site.register(User, UsersAdmin)
