from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


# 1. Создать 3 юзера с именами Alex, Ann, Kate и возрастом 35, 30, 25 лет соответственно
alex = User.objects.create(name='Alex', age=35)
ann = User.objects.create(name='Ann', age=30)
kate = User.objects.create(name='Kate', age=25)


# 2. Создать 2 поста юзеру Alex и 1 пост - юзеру Kate
Post.objects.create(user=alex, title='Post 1 for Alex')
Post.objects.create(user=alex, title='Post 2 for Alex')
Post.objects.create(user=kate, title='Post for Kate')


# 3. Создать 5 комментариев: 2 на 1-й пост юзера Alex, 3 других - на единственный пост юзера Kate.
Comment.objects.create(post=Post.objects.get(user=alex, title='Post 1 for Alex'), text='Comment 1 for Alex')
Comment.objects.create(post=Post.objects.get(user=alex, title='Post 1 for Alex'), text='Comment 2 for Alex')
Comment.objects.create(post=Post.objects.get(user=kate, title='Post for Kate'), text='Comment 1 for Kate')
Comment.objects.create(post=Post.objects.get(user=kate, title='Post for Kate'), text='Comment 2 for Kate')
Comment.objects.create(post=Post.objects.get(user=kate, title='Post for Kate'), text='Comment 3 for Kate')


# 4. Написать запрос, который выбирает все посты,
#    у которых имя Юзера начинается с буквы 'a' (регистр не важен) и заканчивается буквой 'x' (регистр важен),
#    результат отсортировать по полю title у поста, сортировка по убыванию
posts = Post.objects.filter(user__name__istartswith='a', user__name__endswith='x').order_by('-title')


# 5. Получить все комментарии к каждому из постов, удалить самый первый комментарий, а затем добавить новый комментарий
for post in posts:
    comments = Comment.objects.filter(post=post)
    first_comment = comments.first()
    if first_comment:
        first_comment.delete()

    Comment.objects.create(post=post, text='New Comment')


# 6. Добавить лайк на самый свежий комментарий
newest_comment = Comment.objects.latest('id')
newest_comment.likes += 1
newest_comment.save()


# *6. Получить всех Юзеров из БД, у которых количество лайков >= 1
users_with_likes = User.objects.annotate(total_likes=models.Sum('post__comment__likes')).filter(total_likes__gte=1)