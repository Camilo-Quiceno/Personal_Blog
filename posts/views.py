"""Posts viesw's"""

#Django

from django.views.generic import  TemplateView, ListView, DetailView
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
    

class FeedView(ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 3
    context_object_name = 'posts'


    def get_queryset(self):

        queryset = Post.objects.raw(
        """SELECT users_post.id AS id,users_post.title, DATE(users_post.date_created), GROUP_CONCAT(users_tag.tag_name) as Tags, auth_user.id AS User_id
        FROM users_post
	        INNER JOIN users_post_tag ON users_post.id = users_post_tag.post_id
            INNER JOIN users_tag ON users_tag.id = users_post_tag.tag_id
            INNER JOIN auth_user on auth_user.id = users_post.user_id
            GROUP BY users_post.id
            HAVING User_id = {};""".format(self.request.user.id)
        )
        
    
        print(queryset)
    
        return queryset

def PostDetailView(request,pk):
    """Return post detail."""

    queryset = Post.objects.raw(
        """SELECT users_post.id,users_post.title, DATE(users_post.date_created) as Date, GROUP_CONCAT(users_tag.tag_name) as Tags, users_category.category_name as Category, users_post.content as Content
            FROM users_post
                INNER JOIN users_post_tag ON users_post.id = users_post_tag.post_id
                INNER JOIN users_tag ON users_tag.id = users_post_tag.tag_id
                INNER JOIN users_category ON users_category.id = users_post.category_id
            GROUP BY users_post.id
        ;"""
        )
        
    for post in queryset:
        if post.id == pk:
            return render(request, 'posts/postdetail.html',
            {
            'title': post.title,
            'category': post.Category,
            'tags': post.Tags,
            'text': post.Content
            }
            )
            
            break  
    
    return render(request, 'posts/postdetail.html')

    

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