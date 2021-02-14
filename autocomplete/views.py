from autocomplete import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView
from django.views.generic.list import ListView
from . import models
from django.urls import reverse_lazy

# Create your views here.
def autocomplete(req):
    if 'term' in req.GET:
        queryset = models.ChatSearch.objects.filter(title__icontains=req.GET.get('term')).values('title')
        terms = [term.get('title') for term in queryset]
        # terms = [term for term in terms if req.GET.get('term') in term ]
        return JsonResponse(terms, safe=False)
    return render(req, 'autocomplete/index.html')

class SuggestionCreateView(CreateView):
    model = models.ChatSearch
    template_name = 'autocomplete/add.html'
    fields = ['title']
    success_url = reverse_lazy('list')

class SuggestionListView(ListView):
    queryset = models.ChatSearch.objects.all()
    context_object_name = 'suggestions'