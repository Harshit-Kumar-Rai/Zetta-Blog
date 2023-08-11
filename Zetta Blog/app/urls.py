from django.urls import path
from . import views

urlpatterns = [ path('', views.home, name='home'),
               path('readmore/<int:id>', views.readMore, name='readmore'),
               path('like/<int:id>', views.like, name='like'),
               path('bycat/<int:cat>', views.by_cat, name='bycat'),
               ]