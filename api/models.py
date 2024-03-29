from django.db import models
from .validators import validate_user_is_service
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
    icon = models.FileField(verbose_name="Иконка", upload_to="categories/icons/", default="", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryHashtag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="hashtags")
    tag = models.CharField(verbose_name="Название тега", max_length=255)

    def __str__(self):
        return f"{self.category}: {self.tag}"

    class Meta:
        verbose_name = "Хештег"
        verbose_name_plural = "Хештеги"


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
    title = models.CharField(verbose_name="Заголовок статьи", max_length=155, default="", blank=True, null=True)
    body = models.TextField(verbose_name="Описание заявки", blank=True, null=True)
    location = models.CharField(verbose_name="Локация", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    photo = models.ImageField(verbose_name="Фото", upload_to="requests/photos/", null=True, blank=True)
    photo2 = models.ImageField(verbose_name="Фото 2", upload_to="requests/photos/", null=True, blank=True)
    photo3 = models.ImageField(verbose_name="Фото 3", upload_to="requests/photos/", null=True, blank=True)
    photo4 = models.ImageField(verbose_name="Фото 4", upload_to="requests/photos/", null=True, blank=True)
    photo5 = models.ImageField(verbose_name="Фото 5", upload_to="requests/photos/", null=True, blank=True)
    photo6 = models.ImageField(verbose_name="Фото 6", upload_to="requests/photos/", null=True, blank=True)
    photo7 = models.ImageField(verbose_name="Фото 7", upload_to="requests/photos/", null=True, blank=True)
    photo8 = models.ImageField(verbose_name="Фото 8", upload_to="requests/photos/", null=True, blank=True)
    hashtags = models.TextField(verbose_name="Хештег")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="user_requests",
                                 verbose_name="Категория", blank=True, null=True)
    author = models.ForeignKey(SimpleUserProfile, on_delete=models.CASCADE, related_name="user_requests",
                               verbose_name="Автор", blank=True, null=True)

    def __str__(self):
        return f'Заявка от пользователя: {self.author}'

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Story(models.Model):
    preview = models.ImageField(verbose_name="Фото", upload_to="stories/previews/")

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'


class StoryImage(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, verbose_name="История")
    image = models.ImageField(verbose_name="Фото", upload_to="stories/photos/")


class ServiceUserRequestResponse(models.Model):
    service = models.ForeignKey(SimpleUserProfile, on_delete=models.CASCADE, verbose_name="Сервис",
                                validators=[validate_user_is_service])
    user_request = models.ForeignKey(UserRequest, on_delete=models.CASCADE, verbose_name="Заявка пользователя")

    def __str__(self):
        return f"{self.service}: {self.user_request.title}"

    class Meta:
        verbose_name = "Отклик сервиса"
        verbose_name_plural = "Отклики сервиса"

