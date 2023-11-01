from django.contrib import admin
from .models import Category, CategoryHashtag, QuestionAnswer, ImageItem, Region, City, UserRequest, Story, StoryImage


class StoryImageInline(admin.TabularInline):
    model = StoryImage
    extra = 1


class CategoryHashtagAdmin(admin.TabularInline):
    model = CategoryHashtag
    extra = 1


class StoryAdmin(admin.ModelAdmin):
    inlines = [StoryImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    list_display_links = ("pk", "name")
    inlines = [CategoryHashtagAdmin]


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
admin.site.register(Story, StoryAdmin)
