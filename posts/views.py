"""Posts viesw's"""

#Django

from django.views.generic import  TemplateView
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError

#Models
from users.models import Post
from users.models import Category
from users.models import Tag
from users.models import Post_Tag

class WelcomeView(TemplateView):
  
    template_name = 'posts/welcome.html'
    
class FeedView(TemplateView):
  
    template_name = 'posts/feed.html'


def NewPostView(request):

    if request.method == 'POST':

        data = request.POST
        user = data['user']
        title = data['title']
        content = data['content']
        category = data['category']
        tag = data['tag']
        
        tag_list = tag.split(',')

        try:
            obj_category = Category(category_name = category)
            obj_category.save()

        except IntegrityError:
            #messages.error(request, "Case ID not found, Try again!")
            print("Ya existe esa Categoria")
       
        for i in tag_list:
            try:
                obj_tag = Tag(tag_name = i)
                obj_tag.save()
            
            except IntegrityError:
                print("Ya existe ese Tag")

        obj_category_id = Category.objects.get(category_name = category).id
        
        tag_id_list = []
        for i in tag_list:
            obj_tag_id = Tag.objects.get(tag_name = i).id
            tag_id_list.append(obj_tag_id)
        
        obj_post = Post(
            title = title,
            content = content,
            category_id = obj_category_id,
            user_id = user
        )
        obj_post.save()

        obj_post_id = Post.objects.get(title= title).id

        for i in tag_id_list:
            obj_users_post_tag = Post_Tag(
                post_id = obj_post_id,
                tag_id = int(i)
            )

            obj_users_post_tag.save()


    return render(request, 'posts/newpost.html')