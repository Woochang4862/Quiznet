from django.db import models
#from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date=models.DateTimeField('-date published')

    def __str__(self):
        return self.name

class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    #choices = ArrayField(models.CharField(max_length=200))
    answer = models.IntegerField(default=0)
    pub_date=models.DateTimeField('-date published')

    def __str__(self):
        return self.sentence