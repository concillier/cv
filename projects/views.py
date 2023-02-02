from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import articles



#Shows the list of projects in the projects page
def articles_list(request): 
    all_articles = articles.objects.all()
    return render(request, 'projects_list.html', {'all_articles':all_articles})


#Shows the details of each of the projects once a project is clicked on from the articles_list
def detail(request, articles_id): 
    article = get_object_or_404(articles, pk= articles_id)
    return render(request, 'project.html', {'article': article})

