from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import FileResponse
from django.http import HttpResponseRedirect
import os

from .forms import contactform
from django.core.mail import send_mail, BadHeaderError

#Home page
def home(request): 
    return render(request, 'home.html')

#Projects list page
def projects(request):
    return render(request, 'projects.html')

#Contact page first attempt that failed from https://www.youtube.com/watch?v=1ihn3iRXtsY&ab_channel=djangotutorials
# def contact(request): 
#     submitted = False
#     if request.method == 'POST':
#         form = contactform(request.POST)
#         if form.is_valid(): 
#             cd = form.cleaned_data
#             assert False
#             return HttpResponseRedirect ('contact?submitted=True')

#     else:
#             form = contactform()
#             if 'submitted' in request.GET: 
#                 submitted = True

#     return render(request, 'contact.html', {'form': form, 'submitted': submitted})


#Contact page second attempt

def contact(request):
    if request.method == 'POST': 
        form = contactform(request.POST)

        if form.is_valid(): 
            subject = "Website Inquiry"
            body = {
                'Name' : form.cleaned_data['contactname'],
                'Email' : form.cleaned_data['contactemail'],
                'Email_subject' : form.cleaned_data['contactsubject'],
                'Message' : form.cleaned_data['contactmessage'],
            }
            message = "\n".join(body.values())

            try: 
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError: 
                return HttpResponse('Invalid Header found')
            return redirect('home.html')

    form = contactform()
    return render(request, 'contact.html', {'form': form})
