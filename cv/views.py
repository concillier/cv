from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import FileResponse
from django.http import HttpResponseRedirect
import os
from django.contrib import messages

from .forms import ContactForm
from .models import ContactTable

#Function that populates the Home page
def home(request): 
    return render(request, 'home.html')



#Function that populates the Projects list page
def projects(request):
    return render(request, 'projects.html')



#Function that populates the Contact page
#This function: 
# 1. Checks that this is a post request
# 2. A reference to the form is obtained and stored in the variable form
# 3. The form is tested to ensure the values entered are valid.
# 4. The form values are obtained using form.cleaned data and stored in the cd variable
# 5. A new ContactTable object, defined in the models.py file is created and it’s attributes are populated using the values from the form.
# 6. The save method of the object is called.
# All this is done because save() function only applies to model forms.

def contact(request):
    
    if request.method == 'POST': 
        form = ContactForm(request.POST)

        if form.is_valid(): 
            cd = form.cleaned_data

            PortfolioMessage= ContactTable(
                contactname = cd['contactname'],
                contactemail = cd['contactemail'],
                contactsubject = cd['contactsubject'],
                contactmessage = cd['contactmessage']
            )

            PortfolioMessage.save()

            #return a succesful message upon form submission
            messages.success(request, 'Your message has been succesfully sent!')
 
            #or return the homepage upon succesful completion of the contact form
            #return redirect('/')

    else:
        form = ContactForm()


    return render(request, 'contact.html', {
        'form': form
    })
