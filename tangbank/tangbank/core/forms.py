from django import forms

class FormAccount(forms.Form):
    account_name = forms.CharField(label='Nome', max_length=100)
    account_balance = forms.DecimalField(label='Saldo', max_digits=19, decimal_places=2)

class FormWithdrawal(forms.Form):
    withdrawal_name = forms.CharField(label='Nome', max_length=100)
    withdrawal_value = forms.DecimalField(label='Valor do saque', max_digits=19, decimal_places=2)

class FormTransaction(forms.Form):
    transaction_transferring_name = forms.CharField(label='Nome do Transferinte', max_length=100)
    transaction_value = forms.DecimalField(label='Valor do saque', max_digits=19, decimal_places=2)
    transaction_benefited_name = forms.CharField(label='Nome do Beneficiado', max_length=100)

class FormCashier(forms.Form):
    cashier_note1 = forms.IntegerField(label='Cédulas de P$1')
    cashier_note2 = forms.IntegerField(label='Cédulas de P$2')
    cashier_note5 = forms.IntegerField(label='Cédulas de P$5')
    cashier_note10 = forms.IntegerField(label='Cédulas de P$10')
    cashier_note20 = forms.IntegerField(label='Cédulas de P$20')
    cashier_note50 = forms.IntegerField(label='Cédulas de P$50')
    cashier_note100 = forms.IntegerField(label='Cédulas de P$100')