from django.contrib import admin
from .models import Feed,Gallery,Like,Comment,Bookmark,Tag

# Register your models here.
admin.site.register(Feed)
admin.site.register(Gallery)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Bookmark)
admin.site.register(Tag)