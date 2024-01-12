from app1.views import *
from django.urls import path
app_name='1'
urlpatterns=[
    path('page1/',page1,name='page1'),
]