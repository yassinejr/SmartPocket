from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=255)
    amount = models.FloatField()
    category = models.ForeignKey(Category, max_length=255, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.expense_name)

    class Meta:
        verbose_name = 'Expenses'
        verbose_name_plural = 'Expenses'
        ordering = ['-date_added']
