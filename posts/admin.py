from django.contrib import admin

# Register your models here.
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
	list_display =['title', 'updated', 'timestamp']
	list_diplay_links =['title','updated']
	
	list_filter =['updated', 'timestamp']
	search_fields =['title', 'contact']
	
	class Meta:
		model=Post
admin.site.register(Post, PostModelAdmin)