from django.contrib import admin
from .models import Category, Author, Post


# admin.site.register(Author)
admin.site.register(Category)

class PostInfo(admin.ModelAdmin):
    list_display = ['img_tag','title', 'author']

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','/static/js/script.js')


admin.site.register(Post, PostInfo)

class Authorinfo(admin.ModelAdmin):
    list_filter = ['name',]
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','/static/js/script.js')

admin.site.register(Author,Authorinfo)