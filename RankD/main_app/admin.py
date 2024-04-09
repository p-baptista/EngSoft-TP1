from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Review)
admin.site.register(FriendList)
