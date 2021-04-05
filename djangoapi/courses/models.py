from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.FloatField(blank=False, default=0.00)

    def __str__(self):
        return self.name
    