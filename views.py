from django.http import HttpResponse
from django.template import loader

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())
# Create your views here.

def members(request):
  template = loader.get_template('form.html')
  return HttpResponse(template.render())