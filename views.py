from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def members(request):
#     return HttpResponse("Hello world!")
# from django.template import loader

# def members(request):
#   template = loader.get_template('dectionary.html')
#   return HttpResponse(template.render())

def print_hello(request):
 sat_scores={
 'name':'vivanya',
 'age' : 18,
 'place' : 'palakkad',
 }
 return render(request,'dictionary.html',sat_scores)
# Create your views here.
