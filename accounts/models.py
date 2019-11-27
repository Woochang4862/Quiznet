from django.db import models

# Create your models here.
class User(models.Model):
    login_id=models.CharField(max_length=200)
    login_ps=models.CharField(max_length=200)
    nickname=models.CharField(max_length=10)

    def __str__(self):
        return self.login_id

