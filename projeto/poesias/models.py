from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  

class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  #Relacionamento com Autor
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, default=None)
  #Relacionamento ManyToMany com Categoria
  categories = models.ManyToManyField(Category)
  published_date = models.DateField()
  isbn = models.CharField(max_length=13)
  #Campo para upload de imagem
  cover = models.ImageField(upload_to='book_covers/')

  def __str__(self):
    return self.title