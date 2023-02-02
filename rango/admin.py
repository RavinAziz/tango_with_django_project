from django.contrib import admin
from rango.models import Category, Page

class CateogryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
admin.site.register(Category, CateogryAdmin)
admin.site.register(Page, PageAdmin)

