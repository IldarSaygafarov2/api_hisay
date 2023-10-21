from django.contrib import admin
from .models import Category, QuestionAnswer, ImageItem, Region, City, UserRequest


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")


class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ("pk", "question", "answer")
    list_display_links = ("pk", "question")


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ("pk",)


admin.site.register(Region)
admin.site.register(UserRequest)
admin.site.register(City)
admin.site.register(Category, CategoryAdmin)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)
admin.site.register(ImageItem)
