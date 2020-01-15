from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
]