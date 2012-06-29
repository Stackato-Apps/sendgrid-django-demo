from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
  return render_to_response('index.html', {},
      context_instance=RequestContext(request))

@require_POST
def send(request):
  return render_to_response('send.html', {
    'un': request.POST['un'],
    'pw': request.POST['pw'],
    'from': request.POST['from'],
    'to': request.POST['to'],
    'subj': request.POST['subj'],
    'body': request.POST['body'],
    })
