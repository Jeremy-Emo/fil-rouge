from django.conf import settings
import os

def version(request):
    return {'VERSION_NUMBER': os.environ['VERSION']}

def img_path(request):
    return {'IMG_PATH': os.environ['API_IMG_PATH']}


def appli_info(request):
    return {
        'TITRE': os.environ['TITRE']
    }
