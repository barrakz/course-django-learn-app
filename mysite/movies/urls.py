from django.urls import path

from movies import views

app_name = "movies"

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index-movies"),
    path("actors-class-view/", views.ActorView.as_view(), name="actors-class-view"),
    path(
        "actors-template-view/", views.ActorTemplateView.as_view(), name="actors-template-view"
    ),
    # path("actors-list-view/", views.ActorListView.as_view(), name="actors-list-view"),
    path("countries-class-view/", views.CountryView.as_view(), name="countries-class-view"),
    path(
        "countries-template-view/",
        views.CountryTemplateView.as_view(),
        name="countries-template-view"
    ),
    path("countries-list-view/", views.CountryListView.as_view(), name="countries-list-view"),
    path("movies-class-view/", views.MovieView.as_view(), name="movies-class-view"),
    path(
        "movies-template-view/",
        views.MovieTemplateView.as_view(),
        name="movies-template-view"
    ),
    path("movies-list-view/", views.MovieListView.as_view(), name="movies-list-view"),
    path("oscars-class-view/", views.OscarView.as_view(), name="oscars-class-view"),
    path(
        "oscars-template-view/",
        views.OscarTemplateView.as_view(),
        name="oscars-template-view"
    ),
    path("oscars-list-view/", views.OscarListView.as_view(), name="oscars-list-view"),
]