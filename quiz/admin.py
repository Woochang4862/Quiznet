from django.contrib import admin
from quiz.models import Quiz, Category, Choice

admin.site.register(Quiz)
admin.site.register(Category)
admin.site.register(Choice)