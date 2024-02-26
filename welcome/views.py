from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def welcome(request):
    context = {}
    template = loader.get_template("welcome/welcome.html")
    return HttpResponse(template.render(context))
