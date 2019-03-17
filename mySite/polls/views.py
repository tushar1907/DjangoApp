from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Awesome job guys")

def detail(request, question_id):
    return HttpResponse("This is the detail view: %s" %question_id);


def result(request, question_id):
    return HttpResponse("This is the result view: %s" %question_id);


def vote(request, question_id):
    return HttpResponse("This is the vote view: %s" %question_id);