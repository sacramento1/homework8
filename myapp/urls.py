from django.urls import path
from .views import main

urlpatterns = [
    path('post/', main, name='main'),
    # path('post/<str:pk>', detail, name='detail')
]
