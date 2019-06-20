from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
import requests, os, datetime
from public.models import *

# Fonction de log - dev
import logging
logger = logging.getLogger(__name__)
#logger.error('test')

# Home
def index(request):
    url = os.environ['API_BASE_URL'] + "discover/movie"
    now = datetime.datetime.now()

    payload = {
        'include_adult': 'false',
        'include_video': 'false',
        'api_key' : os.environ['API_KEY'],
        'language' : 'fr-FR',
        'sort_by' : 'release_date.desc',
        'page' : '1',
        'release_date.lte' : now.strftime("%Y-%m-%d")
    }
    req = requests.get(url, params=payload)
    try:
        json = req.json()
    except:
        json = {'results' : None}


    return render(request, 'home.html', {
        'json' : json
    })


# Recherche
def search(request):
    url = os.environ['API_BASE_URL'] + "discover/movie"
    now = datetime.datetime.now()

    payload = {
        'include_adult': 'false',
        'include_video': 'false',
        'api_key' : os.environ['API_KEY'],
        'language' : 'fr-FR',
        'page' : '1',
        'release_date.lte' : now.strftime("%Y-%m-%d")
    }
    req = requests.get(url, params=payload)
    try:
        json = req.json()
    except:
        json = {'results' : None}
    return render(request, 'search.html', {
        'json' : json
    })


#Détail
def detail(request, id):
    if request.method == "POST" and not Commentaries.objects.filter(movie_id=id, user_id=request.user).exists():
        commentary = request.POST.get('commentary')
        note = request.POST.get('note')
        Commentaries.objects.create(user_id=request.user, text=commentary, movie_id=id, note=note)

    url = os.environ['API_BASE_URL'] + "movie/" + str(id)
    payload = {
        'api_key' : os.environ['API_KEY'],
        'language' : 'fr-FR',
    }
    req = requests.get(url, params=payload)
    try:
        json = req.json()
    except:
        json = "test"

    commentaries = Commentaries.objects.filter(movie_id=id).order_by('-created_at')

    if not request.user.is_authenticated:
        error_message = "Vous devez être connecté pour noter ce film."
    elif Commentaries.objects.filter(movie_id=id, user_id=request.user).exists():
        error_message = "Vous avez déjà noté ce film."
    else:
        error_message = False

    favorites = Favorites.objects.filter(user_id=request.user)
    favoris = []
    for fav in favorites:
        favoris.append(fav.movie_id)


    return render(request, 'detail.html', {
        'json' : json,
        'commentaries' : commentaries,
        'error_message' : error_message,
        'favoris' : favoris,
    })


#Contact
def contact(request):
    if request.method == "POST":
        text = request.POST.get('contact')
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        Contact.objects.create(user_id=user, text=text)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'contact.html', {})


#Favoris
@login_required
def favoris(request):
    favorites = Favorites.objects.filter(user_id=request.user)
    favoris = []
    for fav in favorites:
        try:
            url = os.environ['API_BASE_URL'] + "movie/" + str(fav.movie_id)
            payload = {
                'api_key' : os.environ['API_KEY'],
                'language' : 'fr-FR',
            }
            req = requests.get(url, params=payload)
            json = req.json()
            liste = {
                'id' : json["id"],
                'nom' : json["title"],
            }
            favoris.append(liste)
        except:
            pass
    return render(request, 'favoris.html', {
        'favoris' : favoris,
    })
