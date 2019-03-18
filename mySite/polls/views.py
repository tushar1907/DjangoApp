from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('pub_date')    
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("This is the detail view: %s" %question_id)


def result(request, question_id):
    return HttpResponse("This is the result view: %s" %question_id)


def vote(request, question_id):
    return HttpResponse("This is the vote view: %s" %question_id)