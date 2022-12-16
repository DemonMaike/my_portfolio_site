from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns =  [
    path('', blog, name='blog'),
    path('<int:blog_id>/', detail, name='detail'),
]