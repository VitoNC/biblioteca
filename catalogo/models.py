from django.db import models

# Create your models here.


class Book(models.Model):
    '''
    Libro para aplicacion de biblioteca
    '''
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    fecha = models.DateField(
        help_text='Fecha de publicación', null=True, blank=True)

    # Relaciones
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Autor')
    genre = models.ManyToManyField('Genre', verbose_name='Género')

    def __str__(self):
        return self.title

    def muestra_genero(self):
        '''Muestra genero para admin'''
        return ', ' .join([gen.name for gen in self.genre.all()[:3]])

    muestra_genero.short_description = 'Género'

    class Meta:
        verbose_name = 'Libro'


class Genre(models.Model):
    name = models.CharField("Género", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Género'


class Author(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    muerte = models.DateField('Fallecido', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}{self.apellidos}'

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
