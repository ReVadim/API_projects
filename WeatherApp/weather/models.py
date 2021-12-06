from django.db import models


class City(models.Model):
    """ City class """

    name = models.CharField(verbose_name='city_name', max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
