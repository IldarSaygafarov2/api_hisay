from django.db import models


# class Service(models.Model):
#     name = models.CharField(verbose_name="Сервис", max_length=150)
#
#     def __str__(self):
#         return self.name
#
#
# class ServiceHashtag(models.Model):
#     name = models.CharField(verbose_name="Хештег", max_length=255)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")
#
#     def __str__(self):
#         return self.name
