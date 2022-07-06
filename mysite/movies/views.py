from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.views.generic import ListView, TemplateView
from django.shortcuts import render

from movies.models import Actor, Country, Movie, Oscar


class IndexView(TemplateView):
    template_name = "movies/index.html"


class ActorView(View):
    def get(self, request):
        return render(
            request,
            template_name="movies/actors.html",
            context={"actors": Actor.objects.all()}
        )


class ActorTemplateView(TemplateView):
    template_name = "movies/actors.html"
    extra_context = {"actors": Actor.objects.all()}


# class ActorListView(ListView):
#     template_name = "movies/list_view.html"
#     model = Actor


class CountryView(View):
    def get(self, request):
        return render(
            request,
            template_name="movies/countries.html",
            context={"countries": Country.objects.all()}
        )


class CountryTemplateView(TemplateView):
    template_name = "movies/countries.html"
    extra_context = {"countries": Country.objects.all()}


class CountryListView(ListView):
    template_name = "movies/list_view.html"
    model = Country


class MovieView(PermissionRequiredMixin,View):
    permission_required = "polls.view_poll"
    def get(self, request):
        return render(
            request,
            template_name="movies/movies.html",
            context={"movies": Movie.objects.all()}
        )


class MovieTemplateView(TemplateView):
    template_name = "movies/movies.html"
    extra_context = {"movies": Movie.objects.all()}


class MovieListView(ListView):
    template_name = "movies/list_view.html"
    model = Movie


class OscarView(View):
    def get(self, request):
        return render(
            request,
            template_name="movies/oscars.html",
            context={"oscars": Oscar.objects.all()}
        )


class OscarTemplateView(TemplateView):
    template_name = "movies/oscars.html"
    extra_context = {"oscars": Oscar.objects.all()}


class OscarListView(ListView):
    template_name = "movies/list_view.html"
    model = Oscar
