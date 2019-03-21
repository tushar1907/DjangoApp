from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('pub_date')    
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    return HttpResponse("This is the result view: %s" %question_id)


def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request,'polls/detail.html', {'question':question, 'error_message': "Please select a choice"})
    else: 
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:reverse', args=(question_id)))