from django.contrib import admin

# Register your models here.
from movies.models import Actor, Country, Movie, Oscar

admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Movie)
admin.site.register(Oscar)
