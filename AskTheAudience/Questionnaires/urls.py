from django.urls import path

from . import views

app_name = 'questionnaires'

urlpatterns = [
    path('', views.index, name='index'),
    path('vote.html', views.vote, name='vote'),
    path('results.html', views.results, name='results'),
]
