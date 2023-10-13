from django.db import models

from accounts.models import SimpleUserProfile


class Region(models.Model):
    name = models.CharField(verbose_name="Название области или региона", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион/Область"
        verbose_name_plural = "Регионы/Области"


class City(models.Model):
    name = models.CharField(verbose_name="Название города", max_length=255, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return f'{self.region}: {self.name}'

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=155, unique=True)
    icon = models.FileField(verbose_name="Иконка", upload_to="categories/icons/", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField(verbose_name="Подкатегория", max_length=155, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories",
                                 verbose_name="Категория")

    def __str__(self):
        return f"{self.category}: {self.name}"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


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


class UserRequest(models.Model):
    body = models.TextField(verbose_name="Описание заявки")
    location = models.CharField(verbose_name="Город", max_length=255)
    price = models.CharField(verbose_name="Цена", max_length=255, default="Договорная")
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    photo = models.ImageField(verbose_name="Фото", upload_to="requests/photos/", null=True, blank=True)
    hashtags = models.TextField(verbose_name="Хештег")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="user_requests",
                                 verbose_name="Категория")
    author = models.ForeignKey(SimpleUserProfile, on_delete=models.CASCADE, related_name="user_requests",
                               verbose_name="Автор")

    def __str__(self):
        return f'Заявка от пользователя: {self.author}'

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
