from django.urls import path
from home.views import *

app_name='anything'

urlpatterns=[
        path('home/',home,name='home')

]