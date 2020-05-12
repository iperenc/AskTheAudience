from django.shortcuts import get_object_or_404, render
from Questionnaires.models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    stuff_for_frontend = {
        'question_list' : question_list,
    }
    return render(request, "Questionnaires/index.html", stuff_for_frontend)

def vote(request):
    question = get_object_or_404(Question, pk=request.GET['question_id'])
    return render(request, "Questionnaires/vote.html", {'question' : question})
