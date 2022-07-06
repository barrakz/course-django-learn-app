from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

from .views import HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls_api')),
    path('homepage/', HomepageView.as_view(), name='homepage'),
    path('polls/', include('polls.urls')),
    path('polls/', include('polls.urls_class')),
    path('movies/', include('movies.urls')),
    path('movies/', include('movies.urls_class')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    # path('accounts/login', LoginView.as_view(), name='login'),

]

