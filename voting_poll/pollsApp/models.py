# In models.py

from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    @property
    def total_votes(self):
        return sum(option.votes for option in self.options.all())

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
