from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request, "computergrid/index.html", {"title": "Project Pineapple", "heading1": "may the force be with you"} )
