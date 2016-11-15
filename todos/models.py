from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='todos', default=1)

    def __str__(self):
        return str(self.text)