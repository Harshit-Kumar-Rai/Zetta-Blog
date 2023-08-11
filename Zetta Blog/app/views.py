from django.shortcuts import render,redirect
from . models import *

def home(request):

    data = Post.objects.all().order_by('-id')
    popular = Post.objects.all().order_by('-views')[:5]
    cat = Category.objects.all()
    author = Author.objects.all().order_by('-views')[:3]
    
    
    return render(request, 'index.html', {
                                            'data':data, 
                                            'cat':cat,
                                            'author':author,
                                            'popular':popular
                                        }
                )

def readMore(request, id):

    data = Post.objects.get(id = id)
    data.views += 1
    
    data.author.views +=1
    data.author.save()
    data.save()

    return render(request, 'readmore.html',{'data':data})

def like(request, id):
    data = Post.objects.get(id = id)
    data.likes += 1
    data.views -= 1
    data.save()
    return redirect('/readmore/{}'.format(id))

def by_cat(request, cat):
    print(cat)

    data = Post.objects.all().filter(cat = cat)
    
    return render(request,'category.html', {'data':data} )