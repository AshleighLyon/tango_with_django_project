from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
# Add another class just do same as below calling
# the admin.site.register() method.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
