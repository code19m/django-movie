from django.urls import path
from django.views.generic.base import View

from . import views


urlpatterns = [
    path("", views.MoviesView.as_view(), name="movie_list"),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("rewiews/<int:pk>/", views.CommentView.as_view(), name="comment"),
]
