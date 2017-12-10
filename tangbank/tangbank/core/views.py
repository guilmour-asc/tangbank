from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'user': 'Guilmour'})
def teste(request):
    return HttpResponse("teste msm")