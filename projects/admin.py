from django.contrib import admin
from .models import articles
from cv.models import ContactTable

# Register your models here.

admin.site.register(articles)
admin.site.register(ContactTable)
