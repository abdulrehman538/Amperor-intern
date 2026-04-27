from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name