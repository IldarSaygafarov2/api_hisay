from django.contrib import admin
from .models import Category, QuestionAnswer, ImageItem

# Register your models here.


admin.site.register(Category)
admin.site.register(QuestionAnswer)
admin.site.register(ImageItem)

