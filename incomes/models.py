from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Source(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    source_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.source_name)


class Incomes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_name = models.CharField(max_length=255)
    amount = models.FloatField()
    source = models.ForeignKey(Source, max_length=255, on_delete=models.CASCADE)
    date_added = models.DateTimeField()

    def __str__(self):
        return str(self.income_name)

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
        ordering = ['-date_added']
