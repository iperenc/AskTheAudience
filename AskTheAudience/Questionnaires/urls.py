from django.urls import path

from . import views

app_name = 'questionnaires'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vote.html', views.vote, name='vote'),
    path('results.html', views.results, name='results'),
    path('new_question.html', views.NewQuestionView.as_view(), name='new_question'),
]
