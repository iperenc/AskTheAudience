from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.text

class Answer(models.Model):

    text = models.CharField(max_length=200)
    votes_number = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
