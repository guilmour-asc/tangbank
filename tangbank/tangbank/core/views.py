from django.shortcuts import render
from django.http import response
from .models import Account, Cashier
from .forms import FormAccount, FormCashier, FormWithdrawal, FormTransaction

def home(request):
    context = {}
    cashier = Cashier
    
    if len(Cashier.objects.all()) == 0:
        cashier.objects.create()
    else:
        cashier = cashier.objects.get(id=1)
    
    accounts = Account.objects.all()
    if request.method == 'POST':
        form_account = FormAccount(request.POST)
        form_cashier = FormCashier(request.POST)
        if form_account.is_valid():
            context['is_valid'] = True
            form_account.post(form_account.cleaned_data)
            form_account = FormAccount()
    else:
        form_account = FormAccount()
        form_cashier = FormCashier()
    context['accounts'] = accounts
    context['cashier'] = cashier
    context['form_account'] = form_account
    context['form_cashier'] = form_cashier
    return render(request, 'home.html', context)
def teste(request):
    return HttpResponse("teste msm")