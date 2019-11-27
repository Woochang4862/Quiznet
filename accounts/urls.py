from django.urls import path
from accounts import views

app_name='accounts'
urlpatterns=[
    path('edit/',views.edit,name='edit'),
    path('profile/',views.profile,name='profile'),
    path('signin/',views.siginin,name='signin'),
    path('signup/',views.signup,name='signup'),
    

]