from django.contrib import admin
from .models import Category, Author, Book
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'published_date',)
  list_filter = ('author', 'categories', 'published_date',)
  search_fields = ('title', 'author__name', 'categories__name',)
  readonly_fields = ('cover_preview',)

  def cover_preview(self, obj):
    return mark_safe(f'<img src="{obj.cover.url}" width="100"/>')
  cover_preview.short_description = "Cover Preview"