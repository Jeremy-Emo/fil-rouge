from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import ajax

urlpatterns = [
    path('recherche', views.search, name='search'),
    path('search', ajax.search, name='ajax_search'),
]