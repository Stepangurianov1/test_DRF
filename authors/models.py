from django.db import models


class ObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


# Create your models here.
class Authors(models.Model):
    objects = ObjectsManager()
    # name = models.CharField(max_length=3)
    first_name = models.CharField(max_length=64)
    # name = models.CharField(max_length=4)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name},  {self.last_name}'


class Biographies(models.Model):
    objects = ObjectsManager()
    text = models.TextField(blank=True, null=True)
    authors = models.OneToOneField(Authors, on_delete=models.CASCADE)


class Book(models.Model):
    objects = ObjectsManager()
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(Authors)
