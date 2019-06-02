from django.conf import settings
import os

def version(request):
    return {'VERSION_NUMBER': os.environ['VERSION']}
