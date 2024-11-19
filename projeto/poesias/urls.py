from django.contrib import admin
from django.urls import path
import poesias.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root_view),
    path('sobre/', views.my_view),
    path('user/<str:username/', views.user_view),
    path('home/', views.home),
    path('page_extends/', views.pextends),
    path('poema_detail/', views.poema_detail),
    path('poema_list/', views.poema_list),
    path('poemas/categorias/<int:category_id>', views.category, name='category_id'),
    path('poemas/autor/<int:author_id>', views.author, name='author_id'),
    path('poemas/categorias404/<int:category_id>', views.category_404, name='category_id'),
]