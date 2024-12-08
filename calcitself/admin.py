from django.contrib import admin
from .models import History, TypeOfOrder

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(History)
admin.site.register(TypeOfOrder)