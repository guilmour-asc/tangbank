from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Account, Cashier, Transaction
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

def conta(request, pk, option=None):
    context = {}
    showDict = {'change': False, 'withdraw': False, 'transfer': False, 'extract': False}
    showDict[option] = True
    account = get_object_or_404(Account, pk=pk)
    history = Transaction.objects.filter(account_id=pk)
    if 'withdrawal' in option:
        temp = option.split('-')
        comb = temp[2].split('_')
        comb = list(int(x) for x in comb)
        Transaction.objects.postWithdraw(account.id, int(temp[1]))
        Account.objects.postWithdraw(account.id, int(temp[1]))
        Cashier.objects.postWithdraw(comb)
        context['withdrawalSuccess'] = True
    
    if request.method == 'POST':
        form_account = FormAccount(request.POST)
        form_withdrawal = FormWithdrawal(request.POST)
        form_transaction = FormTransaction(request.POST)
        
        if form_account.is_valid():
            context['is_valid'] = True
            form_account.update(account.id, form_account.cleaned_data)
            account = get_object_or_404(Account, pk=pk)
            form_account = FormAccount()
        
        if form_withdrawal.is_valid():
            context['is_valid'] = True
            if form_withdrawal.cleaned_data['withdrawal_value'] > account.balance:
                context['response'] = "O valor do saque é maior que teu saldo..."
            else:
                combination, combinationAlt, response = form_withdrawal.getCombinations(form_withdrawal.cleaned_data['withdrawal_value'])
                context['response'] = response
                context['withdrawal'] = form_withdrawal.cleaned_data['withdrawal_value']
                if combination:
                    context['withdrawalData1'] = 'withdrawal-' + str(context['withdrawal']) + '-' + '_'.join(str(x) for x in combination)
                    if combinationAlt:
                        context['withdrawalData2'] = 'withdrawal-' + str(context['withdrawal']) + '-' + '_'.join(str(x) for x in combinationAlt)
                context['combination'] = combination
                context['combinationAlt'] = combinationAlt
                context['choice'] = 0
                form_withdrawal = FormWithdrawal()
        
        if form_transaction.is_valid():
            context['is_valid'] = True
            form_transaction.post(account.id, form_transaction.cleaned_data)
            account = get_object_or_404(Account, pk=pk)
            form_transaction = FormTransaction()
    
    else:
        form_account = FormAccount()
        form_withdrawal = FormWithdrawal()
        form_transaction = FormTransaction()
    context['account'] = account
    context['history'] = history
    context['showDict'] = showDict
    context['form_account'] = form_account
    context['form_withdrawal'] = form_withdrawal
    context['form_transaction'] = form_transaction
    return render(request, 'account.html', context)

def caixa(request):
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