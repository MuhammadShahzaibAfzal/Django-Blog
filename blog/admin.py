from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','add_date')
    search_fields = ('title',)
    list_per_page = 3

    class Media:
        js = ('https://cdn.tiny.cloud/1/ayy6u9xammtrz6c9zr2hrp001le1eholuy5qjfi4rl2w59sw/tinymce/6/tinymce.min.js','js/script.js')

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','add_date')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page= 3

    class Media:
        js = ('https://cdn.tiny.cloud/1/ayy6u9xammtrz6c9zr2hrp001le1eholuy5qjfi4rl2w59sw/tinymce/6/tinymce.min.js','js/script.js')



admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Contact)