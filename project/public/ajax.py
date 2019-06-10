from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests, os, datetime, json

# Fonction de log - dev
import logging
logger = logging.getLogger(__name__)
#logger.error('test')

@csrf_exempt
def search(request):
    if request.is_ajax():
        searchString = request.POST.get('searchString')
        page = str(request.POST.get('page'))
        order = request.POST.get('order')
        if page == "" or page is None:
            page = "1";

        try:
            now = datetime.datetime.now()
            if searchString == "":
                url = os.environ['API_BASE_URL'] + "discover/movie"
                payload = {
                    'include_adult': 'false',
                    'include_video': 'false',
                    'api_key' : os.environ['API_KEY'],
                    'language' : 'fr-FR',
                    'sort_by' : order,
                    'page' : page,
                    'release_date.lte' : now.strftime("%Y-%m-%d")
                }
            else:
                url = os.environ['API_BASE_URL'] + "search/movie"
                payload = {
                    'api_key' : os.environ['API_KEY'],
                    'language' : 'fr-FR',
                    'sort_by' : order,
                    'page' : page,
                    'release_date.lte' : now.strftime("%Y-%m-%d"),
                    'query' : searchString
                }

            req = requests.get(url, params=payload)
            films = []
            res = req.json()
            for result in res["results"]:
                if result["poster_path"] is not None:
                    img = os.environ['API_IMG_PATH'] + result["poster_path"]
                else:
                    img = "/static/img/movies/default.png"
                liste = {
                    'poster_path' : img,
                    'title' : result["title"],
                    'link' : "/films/detail/" + str(result["id"])
                }
                films.append(liste)


            json_data = json.dumps({
                "success": True,
                "films": films,
                "pages": res["total_pages"],
                "nbre_results" : res["total_results"],
            })
        except:
            json_data = json.dumps({
                "success": False,
                "error_message": "Une erreur est survenue."
            })
        return HttpResponse(json_data, content_type="application/json")
    else:
        return Http404()
