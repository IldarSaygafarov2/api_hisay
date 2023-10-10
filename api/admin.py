from django.contrib import admin
from .models import Category, QuestionAnswer, ImageItem, Region, City

# Register your models here.


admin.site.register(Region)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(QuestionAnswer)
admin.site.register(ImageItem)

