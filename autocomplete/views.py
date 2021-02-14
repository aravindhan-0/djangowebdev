from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def autocomplete(req):
    if 'term' in req.GET:
        terms = ['python', 'javascript', 'julia']
        terms = [term for term in terms if req.GET.get('term') in term ]
        return JsonResponse(terms, safe=False)
    return render(req, 'autocomplete/index.html')