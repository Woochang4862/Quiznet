from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date=models.DateTimeField('-date published')

    def __str__(self):
        return self.name

class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    answer = models.IntegerField(default=0)
    pub_date = models.DateTimeField('-date published')

    def __str__(self):
        return self.sentence

class Choice(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text