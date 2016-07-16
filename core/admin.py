from django.contrib import admin
from .models import *
from  tibinade_server.settings import *
admin.site.site_header = ADMIN_SITE_TITLE
admin.site.register(ItemMaster)
admin.site.register(CharaMaster)
admin.site.register(BallonMaster)