from django.urls import path
from quiz import views

urlpatterns = [
    path('<int:>/', admin.site.urls),
]
