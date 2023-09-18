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