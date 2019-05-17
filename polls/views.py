from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're the polls index.")


def detail(request, question_id):
    return HttpResponse("Hello, world. You're the polls detail.")


def results(request, question_id):
    return HttpResponse("Hello, world. You're the polls results.")


def vote(request, question_id):
    return HttpResponse("Hello, world. You're the polls vote.")



