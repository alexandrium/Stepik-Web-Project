from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-added_at')   # !!! QuerySet ?

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User)
    # likes = models.ForeignKey(User)

    # class Meta:
    #     db_table = 'questions'
    #     ordering = ['-creation_date']

    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
