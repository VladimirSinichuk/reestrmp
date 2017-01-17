
# -*- coding: utf-8 -*-

from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse




class Album(models.Model):
    # Choices
    STREET_TYPE = (
        ("вул.Шевченка", "вул.Шевченка"),
        ("вул.Садова", "вул.Садова"),
        ("вул.Тургенівська", "вул.Тургенівська"),
        ("вул.Університетська", "вул.Університетська"),
    )
    # Choices
    ADDRESS_TYPE = (
        ("м.Ірпінь", "м.Ірпінь"),
    )
    # Condition
    CONDITION_TYPE = (
        ("Реєстрація", "Реєстрація"),
        ("Зняття з реєстрації", "Зняття з реєстрації")
    )
    first_name = models.CharField("Прізвище", max_length=250, default='')
    middle_name = models.CharField("Ім’я", max_length=250, default='')
    last_name = models.CharField("По батькові",max_length=500, default='')
    date_of_birht = models.CharField("Дата народження",max_length=100, default='')
    place_of_birth = models.TextField("Місце народження", default='')
    address = models.CharField("Місце проживання", max_length=250, choices=ADDRESS_TYPE, default='')
    street = models.CharField("Вулиця",max_length=500, choices=STREET_TYPE, default='')
    house = models.CharField("Будинок",max_length=500, default='')
    date_of_entry = models.CharField("Дата реєстр./зняття", max_length=250, default='')
    condition = models.CharField("Дія", max_length=500, choices=CONDITION_TYPE, default='')
    type_doc = models.CharField("Тип документа", max_length=250, default='')
    seria_doc = models.CharField("Серія документа", max_length=250, default='')
    number_doc = models.CharField("Номер документа", max_length=250, default='')
    date_doc = models.CharField("Дата видачі", max_length=250, default='')
    subject_doc = models.CharField("Суб’єкт, що видав", max_length=250, default='')
    whence_came = models.CharField("Звідки прибув", max_length=250, default='')
    document = models.FileField("Додати документ",)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    def get_absolute_url(self):
        return reverse('reestr:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' - ' + self.middle_name + ' - ' + self.last_name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)


