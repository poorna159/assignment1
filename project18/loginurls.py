from django.urls import path
from login.views import *

app_name='everything'

urlpatterns=[
        path('login/',login,name='login')

]