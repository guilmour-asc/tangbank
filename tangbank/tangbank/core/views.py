from django.shortcuts import render
from django.http import HttpResponse
from .models import Account

def home(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'home.html', context)
def teste(request):
    return HttpResponse("teste msm")