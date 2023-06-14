from django.urls import path
from register.views import *

app_name='something'

urlpatterns=[
        path('register/',register,name='register')

]