from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='User name', max_length=20)
    age = forms.IntegerField(label='User age')
    gender = forms.CharField(label='User gender', max_length=6)
    nationality = forms.CharField(label='User nationality', max_length=100)


class BookForm(forms.Form):
    book_name = forms.CharField(label='Book name', max_length=23)
    book_price = forms.IntegerField(label='Book price')
    book_publisher = forms.CharField(label='Book publisher', max_length=25)



class PublisherForm(forms.Form):
    publisher_name = forms.CharField(label='Publisher name', max_length=13)