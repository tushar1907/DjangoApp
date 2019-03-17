
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date_published')

    def _str__(self):
        return self.question_text


class Choice(models.Model):
    question_text = models.CharField(max_length=100)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def _str__(self):
        return self.choice_text