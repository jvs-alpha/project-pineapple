from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from random import randint

def yindex(request):
    question_list = Question.objects.all()
    return render(request,"index.html",{"question_list":question_list,"title":"Youtube Question List"})

def detail(request,qid):
    question = get_object_or_404(Question,pk=qid)
    return render(request,"detail.html",{"question":question, "title":"Question and Choices"})

def likes(request,yid):
    likes = randint(0,10000)
    return HttpResponse("The video " + str(yid) + " has " + str(likes) + " likes")

def comments(request,yid):
    comments = randint(0,10000)
    return HttpResponse("The video " + str(yid) + " has " + str(comments) + " comments")

# Create your views here.
