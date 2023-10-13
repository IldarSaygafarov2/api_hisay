from django.contrib import admin
from .models import Category, QuestionAnswer, ImageItem, Region, City, Subcategory, UserRequest

# Register your models here.


admin.site.register(Region)
admin.site.register(UserRequest)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(QuestionAnswer)
admin.site.register(ImageItem)

