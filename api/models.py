from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=155, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class QuestionAnswer(models.Model):
    question = models.CharField(verbose_name="Вопрос", max_length=255, unique=True)
    answer = models.TextField(verbose_name="Ответ")
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Вопрос-Ответ"
        verbose_name_plural = "Вопросы-Ответы"



class ImageItem(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to='photos/mainpage/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'