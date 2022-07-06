from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from movies.models import Actor, Movie


# ACTORS CRUD


class ManagerGroupTest(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        manager_group = Group.objects.get(name="Managers")
        return self.request.user.groups.all()



class TwoLettersUpper(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        if self.request.user.username:
            return self.request.user.username[0:2].isupper()
        return False


class IsDigit(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        if self.request.user.username:
            return any(char.isdigit() for char in self.request.user.username)
        return False


class ActorListView(IsDigit, ListView):
    template_name = "movies/list_view.html"
    model = Actor


class ActorCreateView(LoginRequiredMixin, CreateView):
    model = Actor
    fields = "__all__"
    template_name = "movies/form.html"
    success_url = reverse_lazy("movies:actors-list-view")


class ActorDeleteView(DeleteView):
    model = Actor
    template_name = "movies/delete.html"
    success_url = reverse_lazy("movies:actors-list-view")


class ActorUpdateView(UpdateView):
    model = Actor
    fields = ["name", "last_name"]
    template_name = "movies/form.html"
    success_url = reverse_lazy("movies:actors-list-view")


class ActorDetailView(DetailView):
    model = Actor
    template_name = "movies/actor_detail.html"


# MOVIE CRUD

class MoviesListView(ListView):
    template_name = "movies/list_view.html"
    model = Movie


class MovieCreateView(ManagerGroupTest, CreateView):
    model = Movie
    fields = "__all__"
    template_name = "movies/form.html"
    success_url = reverse_lazy("movies:movies-list-view")


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movies/delete.html"
    success_url = reverse_lazy("movies:movies-list-view")


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["title", "year"]
    template_name = "movies/form.html"
    success_url = reverse_lazy("movies:movies-list-view")


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
