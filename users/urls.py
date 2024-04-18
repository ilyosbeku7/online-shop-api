from django.urls import path
from .views import LodinApiView, register

app_name='users'

urlpatterns=[
    path('login/', LodinApiView.as_view(), name='login'),
    path('register/', register,  name='register')
]