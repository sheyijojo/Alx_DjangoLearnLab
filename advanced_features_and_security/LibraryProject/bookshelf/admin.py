from django.contrib import admin
from .models import Book

from .models import CustomUser, CustomerUserAdmin
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year')
admin.site.register(CustomUser, CustomerUserAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    search_fields = ('username', 'email')