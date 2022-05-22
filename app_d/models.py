from sys import float_info
from django.db import models


class SampleModel(models.Model):
    char = models.CharField(max_length=10, blank=True, null=True, verbose_name='Shorter Characters')
    bool = models.BooleanField(default=True, verbose_name='Boolean')
    date = models.DateField(blank=True, null=True, verbose_name='Date')
    longer_char = models.CharField(max_length=255, blank=True, null=True, verbose_name='Longer Characters')
    datetime = models.DateTimeField(blank=True, null=True, verbose_name='Date & Time')
    integer = models.IntegerField(blank=True, null=True, verbose_name='Integer')
    float_info = models.FloatField(blank=True, null=True, verbose_name='Float')
    decimal = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, verbose_name='Decimal Number')
    text = models.TextField(blank=True, null=True, verbose_name='Long Text')