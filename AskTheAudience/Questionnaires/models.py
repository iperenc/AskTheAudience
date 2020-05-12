from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.text
