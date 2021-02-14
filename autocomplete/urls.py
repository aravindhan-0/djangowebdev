from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.autocomplete, name='autocomplete'),
    path('add/', views.SuggestionCreateView.as_view()),
    path('view/', views.SuggestionListView.as_view(), name='list'),
]