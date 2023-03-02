from django import forms


#The form appearing on contact.html, to collect messages that will be saved in Django admin (as added in admin.py)
class ContactForm(forms.Form): 
    contactname = forms.CharField(max_length=40, widget=forms.TextInput(attrs= {
        'class':'form-control form-control-sm'
    }))
    contactemail = forms.EmailField(required= True, widget=forms.EmailInput(attrs= {
        'class':'form-control form-control-sm'
    }))
    contactsubject = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {
        'class':'form-control form-control-sm'
    }))
    contactmessage = forms.CharField(max_length=400, widget=forms.Textarea(attrs= {
        'class':'form-control form-control-sm',
        'rows':'4'
    }))