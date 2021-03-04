
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home, name='home'),
    path('search', views.search, name='search'),
    path('movie',views.movie, name='movie'),
    path('searchm',views.searchm, name='searchm'),
    path('game',views.game,name='game'),
    path('profile',views.profile,name='profile'),
    path('about',views.about,name='about'),
    path('contact',views.about,name='contact'),
    path('software',views.software,name="software"),

]
