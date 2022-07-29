from statistics import mode
from django.db import models

class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Book(models.Model):
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200,primary_key=True)
    price = models.IntegerField()
    price_discount = models.IntegerField(default=0)
    count = models.PositiveIntegerField(default=0)

class Order(models.Model):
    time = models.DateTimeField(null=True)
    total_price = models.PositiveIntegerField(null=True)

class BookInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=0)
