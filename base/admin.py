from django.contrib import admin
from .models import *
from django.apps import apps

models = apps.get_models()

for m in models:
    try:
        admin.site.register(m)
    except admin.sites.AlreadyRegistered:
        pass
