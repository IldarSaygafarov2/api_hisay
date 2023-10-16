from django.contrib import admin
from .models import SimpleUserProfile

# Register your models here.


@admin.register(SimpleUserProfile)
class SimpleUserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fullname')
