from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import FormView, CreateView

from Questionnaires.forms import NewQuestionForm
from Questionnaires.models import *

class IndexView(generic.ListView):
    template_name = 'Questionnaires/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

def vote(request):
    question = get_object_or_404(Question, pk=request.GET['question_id'])
    return render(request, "Questionnaires/vote.html", {'question' : question})

def results(request):
    answer_received = get_object_or_404(Answer, pk=request.POST.get('radio_choice') )
    answer_received.votes_number+=1
    answer_received.save()

    question = get_object_or_404(Question, pk=request.POST['question_id'])
    answer_list = question.answer_set.all()

    all_votes = sum( [a.votes_number for a in answer_list] )

    answer_list_percent = []
    for answer in answer_list:
        answer_list_percent.append( answer.votes_number*100/all_votes )

    front_end_info = {
        'question' : question,
        'answer_list' : zip(answer_list, answer_list_percent),
        'answer_id' : answer_received.id,
        }
    return render(request, "Questionnaires/results.html", front_end_info)

class NewQuestionView(CreateView):
    template_name = 'Questionnaires/new_question.html'
    form_class = NewQuestionForm
    success_url = '/'
