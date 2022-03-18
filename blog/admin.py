from django import forms
from django.contrib import admin


from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Comment)
