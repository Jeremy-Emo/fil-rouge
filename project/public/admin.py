from django.contrib import admin
from public.models import *
from django.apps import apps


# Register your models here.
for model in apps.get_app_config('public').get_models():
    try:
        admin.site.register(model, eval(model.__name__ + "Admin") )
    except:
        admin.site.register(model, None)
