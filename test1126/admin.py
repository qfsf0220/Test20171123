from django.contrib import admin

# Register your models here.

from .models import  Blog,Author

class Arti(admin.ModelAdmin):
    list_display = ('name','email')

class Arti2(admin.ModelAdmin):
    list_display = ("full_name",)

admin.site.register(Author,Arti)
admin.site.register(Blog,Arti2)
