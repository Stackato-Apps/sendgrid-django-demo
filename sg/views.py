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
  username  = request.POST.get('username')
  password  = request.POST.get('password')
  from_addr = request.POST.get('from')
  to_addr   = request.POST.get('to')
  subj      = request.POST.get('subj')
  body      = request.POST.get('body')

  connection = get_connection(username=username, password=password);
  connection.open()

  email = EmailMessage(subj, body, from_addr,
      [to_addr], 
      [], # bcc addresses
      headers = {'Reply-To': from_addr}, # add email headers as a dictionary
      connection=connection)
  email.attach_file(os.path.join(settings.ROOT, 'SendGrid_Deliverability_Guide.pdf'),
      'application/pdf')
  email.send()

  return render_to_response('send.html', {
    'from': from_addr,
    'to': to_addr,
    'subj': subj,
    'body': body,
    }, context_instance=RequestContext(request))
