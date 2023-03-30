from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('post/<str:pk>/',views.post),
    path('category/<str:pk>/',views.category),
    path('posts/',views.posts),
    path('about-us/',views.aboutUs),
    path('contact-us/',views.contactUs),


]
