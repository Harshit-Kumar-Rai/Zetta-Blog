from django.db import models
from django.utils.html import format_html

published = ((True,'Post'),
             (False,"Don't Post", ))

class Category(models.Model):

    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/img/category_img/', null=True)

    def __str__(self):
        return self.name

class Author(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(null=True)
    img = models.ImageField(upload_to='static/img/author_img/', null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    
    id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    short = models.TextField(default='NA')
    date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='static/img/post_img/', null=True)
    is_published = models.BooleanField(choices=published, default=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def img_tag(self):
        print(self.image)
        return format_html(f'<img src="/{self.image}" style="width:40px; height:0px; border-radius:50%;"/>')

