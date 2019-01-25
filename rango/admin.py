from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
# Add another class just do same as below calling
# the admin.site.register() method.

admin.site.register(Category)
admin.site.register(Page)