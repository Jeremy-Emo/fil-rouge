from django.shortcuts import render
import requests, os, datetime

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

    return render(request, 'detail.html', {
        'json' : json
    })
