# from django.db import models
#
#
# class Students(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
# # Create your models here.


from django.db import models


class User(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    nationality = models.TextField()


class Post(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")


class Comment(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


class Like(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)



from my_app.models import User, Post, Comment, Like

# user = User.objects.create(id=1, name='...', age=20, gender='male')  # return created User instance
#
# users_all = User.objects.all()  # Returns QuerySet object
# users_names = [u.name for u in users_all]  # QuerySet is Iterable
# first_user = users_all[0]  # QuerySet supports indexes
# users_all_sql_query = str(users_all.query)  # return underlying SQL query (need to cast it to str)
#
# post = Post.objects.create(id=1, title='', description='', user=first_user)  # need to set User instance to 'user' attribute
# first_post = Post.objects.get(id=1)  # get Post object by specified id
#
# posts = Post.objects.filter(id=1)  # returns QuerySet object with only one Post object inside



class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'se'

class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField(Author)

    class Meta:
        default_related_name = 'books'

    def __str__(self):
        return f'{self.name}, {self.price} $, [publisher: {self.publisher}]'


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    class Meta:
        default_related_name = 'stores'

    def __str__(self):
        return self.name


