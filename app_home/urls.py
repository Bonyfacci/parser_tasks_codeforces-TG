from django.urls import path

from app_home.apps import AppHomeConfig
from app_home.views import home

app_name = AppHomeConfig.name

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/
]
