from django.urls import path
from . import views

urlpatterns = [
    path('<int:articles_id>', views.detail, name='detail'),
]
