from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from faker import Faker
from .models import Book, Author, Category

# Create your views here.
def my_view(request):
    return HttpResponse("Uma teste string de resposta")


def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")


def root_view(request):
    return HttpResponse("Estamos na Raiz 2. Porta 8000")

def home(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={
        'authors': authors,
        'categories': categories
    })

def pextends(request):
    return render(request, 'page_extends.html')

fake = Faker('pt_BR')

def make_poetry():
    return{
        'title': fake.sentence(nb_words=5),
        'full_text': fake.text(250),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'genre': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/320/320/poetry.book',
        },
        'is_popular': fake.boolean()
    }

def poema_detail(request):
    poetry = make_poetry()
    return render(request, 'poema_detail.html', {'poetry': poetry})

def poema_list(request):
    poesias = [make_poetry() for _ in range(5)]
    return render(request, 'poema_list.html', {'poesias': poesias})

def category(request, category_id):
    books = Book.objects.filter(
        categories__id=category_id,
    )

    if not books:
        raise Http404("Not found ")

    return render(request, 'category.html', context={
        'books': books,
        'title': f'Categoria: {books.first().categories.all()[0]}'
    })

def author(request, author_id):
    books = Book.objects.filter(
        author__id=author_id,
    )

    if not books:
        raise Http404("Not found ")

    return render(request, 'author.html', context={
        'books': books,
        'title': f'Autor: {books.first().author.name}'
    })

def category_404(request, category_id):
    books = get_list_or_404(
        Book.objects.filter
        (
            categories__id=category_id,
        )
    )
    print("Books: ", books)
    print("Books: ", books[0])
    print("Books: ", books[0].categories.all()[0])
    return render(request, 'category.html', context={
        'books': books,
        'title': f'Categoria: {books[0].categories.all()[0]}'
    })