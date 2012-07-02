import os
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from django.core.mail import get_connection

# Create your views here.

def index(request):
  return render_to_response('index.html', {},
      context_instance=RequestContext(request))

@require_POST
def send(request):
  from_addr = request.POST['from']
  to_addr = request.POST['to']
  subj = request.POST['subj']
  body = request.POST['body']

  connection = get_connection();
  connection.open()

  email = EmailMessage(subj, body, from_addr,
              [to_addr], [],
              headers = {'Reply-To': from_addr}, connection=connection)
  email.attach_file(os.path.join(settings.ROOT, 'SendGrid_Deliverability_Guide.pdf'),
      'application/pdf')
  email.send()

  return render_to_response('send.html', {
    'from': from_addr,
    'to': to_addr,
    'subj': subj,
    'body': body,
    })
