from django.contrib import admin
from .models import Post,Author,Tag,Comment

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display=('caption',)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')
    
class PostAdmin(admin.ModelAdmin):
    list_display=('title','date','author',)
    list_filter=('author','date','tags',)
    prepopulated_fields = {'slug':('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display=('user_name','user_email','post')
    
admin.site.register(Tag,TagAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
