from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
        if form_cashier.is_valid():
            context['is_valid'] = True
            form_cashier.post(form_cashier.cleaned_data)
            form_cashier = FormCashier()
    else:
        form_account = FormAccount()
        form_cashier = FormCashier()
    context['accounts'] = accounts
    context['cashier'] = Cashier.objects.get(id=1)
    context['form_account'] = form_account
    context['form_cashier'] = form_cashier
    return render(request, 'home.html', context)

def teste(request):
    return HttpResponse("teste msm")

def conta(request, pk):
    showDict = {'change': False, 'withdraw': False, 'transfer': False, 'extract': False}
    account = get_object_or_404(Account, pk=pk)
    context = {'account': account, 'showDict': showDict}
    return render(request, 'account.html', context)

def caixa(request):
    cashier = Cashier.objects.get(id=1)
    context = {}
    context['is_valid'] = False
    if request.method == 'POST':
        form_cashier = FormCashier(request.POST)
        if form_cashier.is_valid():
            context['is_valid'] = True
            form_cashier.post(form_cashier.cleaned_data)
            form_cashier = FormCashier()
    else:
        form_cashier = FormCashier()
    context['cashier'] = Cashier.objects.get(id=1)
    context['form_cashier'] = form_cashier
    context['accounts'] = Account.objects.all()
    context['form_account'] = FormAccount()
    return (render(request, 'cashier.html', context) if context['is_valid'] == False else render(request, 'home.html', context))