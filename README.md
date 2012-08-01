# Sendgrid Django Demo 

A Python Django application that sends email through SendGrid. You'll
need a SendGrid account to use this, which you can get here:

 https://sendgrid.com/user/signup

## Local development

Install Django using 'pip' or 'pypm':

    pypm install django 

Run the server locally:

    python manage.py runserver

## Deploying to Stackato

To push this application to Stackato, target the API endpoint (e.g.
api.stacka.to) then run:

    stackato push -n

## The longer version

There's a blog post about using SendGrid with Stackato here:

 http://www.activestate.com/blog/2012/07/youve-got-mail-using-sendgrid-stackato 

