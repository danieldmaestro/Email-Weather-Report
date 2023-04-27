from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.location

class EmailSub(models.Model):
    name = models.CharField(max_length=50)
    location = models.ManyToManyField('Location', related_name='locations')
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

