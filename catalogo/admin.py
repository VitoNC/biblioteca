from django.contrib import admin

# Register your models here.
from .models import Book, Author, Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'muestra_genero']
    list_filter = ('author',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos']
    fieldsets = (
        ('DATOS PERSONALES',{'fields': ('nombre', 'apellidos')}),
        ('FECHAS',{ 'fields': ('nacimiento', 'muerte')})
    )
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
