from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"


