from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/category/')
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image.url))

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/post/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

    
    def image_tag(self):
        return format_html('<img src="{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image.url))


class Contact(models.Model):
    name =  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name