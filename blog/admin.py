from django.contrib import admin

# Register your models here.
from blog.models import Entry, Category, Tag

admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Tag)
