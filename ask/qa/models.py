from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')
    

class Question(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField(blank = True)
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, blank = True, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name = "likes")
    objects = QuestionManager()

    def __str__(self):
        return self.title
  
    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table = 'question'



class Answer(models.Model):
    text = models.TextField(blank = True)
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question, blank = True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank = True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'answer'
    


