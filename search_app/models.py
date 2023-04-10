from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Ticket(models.Model):
    departure_date = models.DateTimeField(blank=False)
    arrive_date = models.DateTimeField(blank=False)
    train_number = models.CharField(validators=(MinLengthValidator(4),),
                                    max_length=12)
    destination = models.CharField(blank=False, max_length=32)
    departure = models.CharField(blank=False, max_length=32)
    cost = models.PositiveIntegerField()

    class Meta:
        ordering = ('cost',)

    def __str__(self):
        return f'Билет №{self.id}.<br>' \
               f'Дата отправления: {self.departure_date}.<br>' \
               f'Поезд №{self.train_number}.<br>' \
               f'Стоимость: {self.cost}.'

