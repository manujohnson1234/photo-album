from django.contrib import admin

from .models import Category, Album
# Register your models here.


admin.site.register(Album)
admin.site.register(Category)