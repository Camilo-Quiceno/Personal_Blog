from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    
    category_name = models.CharField(max_length=30,unique=True)


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=128, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    content = models.TextField(null=False)

class Tag(models.Model):
    
    tag_name = models.CharField(max_length=30,unique=True)

class Post_Tag(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)