from django.urls import path

from . import views

# base url: instagram/
# this is how we can define url links in instagram app
urlpatterns = [
    path("", views.index, name="index"),
    path("view", views.viewPost, name="viewPost"),
    path("view/<int:postId>/", views.ViewPostById, name="viewPostById"),
    path("users", views.viewUsers, name="viewUsers"),
    path("user/<int:userId>", views.viewUserById, name="viewUserById"),
    path("newPost", views.newPost, name="newPost"),
]