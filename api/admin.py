from django.contrib import admin
from .models import Category, QuestionAnswer, ImageItem, Region, City, Subcategory, UserRequest

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "category")
    list_display_links = ("pk", "name")
    list_filter = ("category",)
    list_editable = ("category",)


class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ("pk", "question", "answer")
    list_display_links = ("pk", "question")


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ("pk", "")

admin.site.register(Region)
admin.site.register(UserRequest)
admin.site.register(City)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(QuestionAnswer, QuestionAnswerAdmin)
admin.site.register(ImageItem)

