from django.urls import path

from . import views

# base url: instagram/
# this is how we can define url links in instagram app
urlpatterns = [
    path("", views.index, name="index"),
]