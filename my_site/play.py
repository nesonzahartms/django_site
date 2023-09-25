import io
from drf_app.models import Book, Publisher, Author
from drf_app.serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import requests


url = "http://127.0.0.1:8000/drf_app/publishers/"


pub_new_data2 = {'id': 15, 'name': 'ApiPublisher2'}
pub_new_data3 = {'id': 16, 'name': 'ApiPublisher3'}


data = [pub_new_data2, pub_new_data3]


resp = requests.post(url=url, json=data)





url = "http://127.0.0.1:8000/auth/users/"

data = {'username': 'zahar2', 'password': 'qwertyuiop1234321', 'email': 'zahar@mail.com'}

resp = requests.post(url=url, json=data)






url = "http://127.0.0.1:8000/auth/jwt/create/"

data = {'username': 'zahar1', 'password': 'qwertyuiop1234321'}

resp = requests.post(url=url, json=data)








from  django.contrib.auth.models import User, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, passord=None, *args, **kwargs):
        return super().create_user(username, email, passord, *args, **kwargs)



class CustomUser(User):
    objects = UserManager()