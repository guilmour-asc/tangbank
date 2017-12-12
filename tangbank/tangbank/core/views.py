from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account, Cashier
from .forms import FormAccount

@csrf_exempt
def home(request):
    cashier = Cashier
    if len(Cashier.objects.all()) == 0:
        cashier.objects.create()
    else:
        cashier = cashier.objects.get(id=1)
    accounts = Account.objects.all()
    if request.method == 'POST':
        form_account = FormAccount(request.POST)
    else:
        form_account = FormAccount()
    context = {'accounts': accounts, 'cashier': cashier, 'form_account': form_account}
    return render(request, 'home.html', context)
def teste(request):
    return HttpResponse("teste msm")