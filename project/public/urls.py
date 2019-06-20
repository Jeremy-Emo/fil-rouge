from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import ajax

urlpatterns = [
    path('recherche', views.search, name='search'),
    path('search', ajax.search, name='ajax_search'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('change_fav', ajax.add_favorite, name='add_favorite'),
    path('favoris', views.favoris, name='favoris'),
]
