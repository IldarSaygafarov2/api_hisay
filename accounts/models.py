from django.db import models

# Create your models here.


class SimpleUserProfile(models.Model):
    tg_username = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Юзер в телеграмме')
    fullname = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='ФИО')
    tg_chat_id = models.BigIntegerField(
        null=True, blank=True, unique=True, verbose_name='Айди пользователя в телеграмме')
    phone_number = models.CharField(
        max_length=15, null=True, blank=True, unique=True, verbose_name='Номер телефона')
    is_service = models.BooleanField(default=False, null=True)
    user_avatar = models.ImageField(
        verbose_name="Фото пользователя", upload_to="users/avatars/", null=True, blank=True)
    rating = models.FloatField(
        verbose_name="Рейтинг сервиса", default=0, blank=True, null=True)
    education = models.TextField(
        verbose_name="Образование", null=True, blank=True)
    info_about = models.TextField(verbose_name="О себе", null=True, blank=True)
    service_photo_certificate = models.ImageField(
        verbose_name="Фото сертификата сервиса", upload_to="services/certificates/", null=True, blank=True)
    # city = models.ForeignKey(
    #     City, on_delete=models.SET_NULL, null=True, blank=True, related_name="cities", verbose_name='Город')
    city = models.CharField(max_length=255, verbose_name="Город", null=True, blank=True)
    is_banned = models.BooleanField(verbose_name="Блокировка", default=False, null=True, blank=True)
    verification_code = models.CharField(
        max_length=6, blank=True, null=True, verbose_name='Код подтверждения')

    def __str__(self):
        if self.is_service:
            return f'Сервис: {self.fullname}'
        return f"{self.fullname}: {self.phone_number}"

    class Meta:
        verbose_name = 'Пользователь приложения'
        verbose_name_plural = 'Пользователи приложения'
