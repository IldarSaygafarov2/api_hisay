from django.contrib import admin
from .models import SimpleUserProfile, ServiceSetting

# Register your models here.


@admin.register(SimpleUserProfile)
class SimpleUserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fullname')


@admin.register(ServiceSetting)
class ServiceSettingAdmin(admin.ModelAdmin):
    pass