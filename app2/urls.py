from app2.views import *
from django.urls import path
app_name='2'

urlpatterns=[
    path('page2/',page2,name='page2'),
]