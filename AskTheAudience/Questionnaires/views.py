from django.shortcuts import get_object_or_404, render
from Questionnaires.models import *

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    stuff_for_frontend = {
        'question_list' : question_list,
    }
    return render(request, "Questionnaires/index.html", stuff_for_frontend)

def vote(request):
    question = get_object_or_404(Question, pk=request.GET['question_id'])
    answer_list = question.answer_set.all()
    return render(request, "Questionnaires/vote.html", {'question' : question, "answer_list" : answer_list})

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
