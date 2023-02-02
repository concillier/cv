from django import forms

class contactform(forms.Form): 
    contactname = forms.CharField(max_length=40, label='Your name')
    contactemail = forms.EmailField(required= True, label= 'Your email address')
    contactsubject = forms.CharField(max_length=50,label= 'Subject')
    contactmessage = forms.CharField(max_length=400, widget=forms.Textarea, label = 'Message')