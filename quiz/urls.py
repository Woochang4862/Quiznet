from django.urls import path
from quiz import views

app_name = 'quiz'
urlpatterns = [
    path('<string:quiz_category>/<int:quiz_number>/', views.display),
]
