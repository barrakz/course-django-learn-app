

from movies import views_class
from django.urls import path

app_name = "movies"

urlpatterns = [
    path("actors-list-view/", views_class.ActorListView.as_view(), name="actors-list-view"),
    path("actor-create-view/", views_class.ActorCreateView.as_view(), name="actor-create-view"),
    path("actor-delete-view/<pk>", views_class.ActorDeleteView.as_view(), name="actor-delete-view"),
    path("actor-update-view/<pk>", views_class.ActorUpdateView.as_view(), name="actor-update-view"),
    path("actor-detail-view/<pk>", views_class.ActorDetailView.as_view(), name="actor-detail-view"),

    path("movies-list-view/", views_class.MoviesListView.as_view(), name="movies-list-view"),
    path("movie-create-view/", views_class.MovieCreateView.as_view(), name="movie-create-view"),
    path("movie-delete-view/<pk>", views_class.MovieDeleteView.as_view(), name="movie-delete-view"),
    path("movie-update-view/<pk>", views_class.MovieUpdateView.as_view(), name="movie-update-view"),
    path("movie-detail-view/<pk>", views_class.MovieDetailView.as_view(), name="movie-detail-view"),

]
