from django.shortcuts import render
import requests, os, datetime

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
