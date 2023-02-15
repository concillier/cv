from django.db import models

# Because the contact form is a simple form, this model is used to link
# to the form to explicitly tell Django what form values to save. 
class ContactTable(models.Model): 
    contactname = models.CharField(max_length=40)
    contactemail = models.EmailField()
    contactsubject = models.CharField(max_length=50)
    contactmessage = models.CharField(max_length=400)

    def __str__(self): 
        return self.contactname
