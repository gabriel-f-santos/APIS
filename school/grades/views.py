from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def grades(request):
    if request.method == 'GET':
        return HttpResponse('my grades')