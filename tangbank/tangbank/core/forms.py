from django import forms
from .models import Account, Cashier, Transaction

class FormAccount(forms.Form):
    account_name = forms.CharField(label='Nome', max_length=100)
    account_balance = forms.DecimalField(label='Saldo', max_digits=19, decimal_places=2)
    
    def post(self, data):
        account = Account(name=data['account_name'], balance=data['account_balance'])
        account.save()
    
    def update(self, affected, data):
        account = Account.objects.get(id=affected)
        account.name = data['account_name']
        account.balance = data['account_balance']
        account.save()

class FormWithdrawal(forms.Form):
    # withdrawal_name = forms.CharField(label='Nome', max_length=100)
    withdrawal_value = forms.DecimalField(label='Valor do saque', max_digits=19, decimal_places=2)

    def combination(self, originalValue):
        value = originalValue
        noteCombination = [0 ,0 ,0 ,0 ,0 ,0 ,0]
        cashier = Cashier.objects.get(id=1)
        if cashier.note100 > 0:
            for i in range(cashier.note100):
                if value >= 100:
                    noteCombination[6] += 1
                    value -= 100
                else:
                    break
        if cashier.note50 > 0:
            for i in range(cashier.note50):
                if value >= 50:
                    noteCombination[5] += 1
                    value -= 50
                else:
                    break
        if cashier.note20 > 0:
            for i in range(cashier.note20):
                if value >= 20:
                    noteCombination[4] += 1
                    value -= 20
                else:
                    break
        if cashier.note10 > 0:
            for i in range(cashier.note10):
                if value >= 10:
                    noteCombination[3] += 1
                    value -= 10
                else:
                    break
        if cashier.note5 > 0:
            for i in range(cashier.note5):
                if value >= 5:
                    noteCombination[2] += 1
                    value -= 5
                else:
                    break
        if cashier.note2 > 0:
            for i in range(cashier.note2):
                if value >= 2:
                    noteCombination[1] += 1
                    value -= 2
                else:
                    break
        if cashier.note1 > 0:
            for i in range(cashier.note1):
                if value >= 1:
                    noteCombination[0] += 1
                    value -= 1
                else:
                    break
        if value != 0:
            return 1
        else:
            return noteCombination
    
    def combinationAlternative(self, originalValue):
        value = originalValue
        noteCombination = [0 ,0 ,0 ,0 ,0 ,0 ,0]
        cashier = Cashier.objects.get(id=1)
        if cashier.note100 > 0:
            cashier.note50 = 0
            for i in range(cashier.note100):
                if value >= 100:
                    noteCombination[6] += 1
                    value -= 100
                else:
                    break
        if cashier.note50 > 0:
            for i in range(cashier.note50):
                if value >= 50:
                    noteCombination[5] += 1
                    value -= 50
                else:
                    break
        if cashier.note20 > 0:
            for i in range(cashier.note20):
                if value >= 20:
                    noteCombination[4] += 1
                    value -= 20
                else:
                    break
        if cashier.note10 > 0:
            for i in range(cashier.note10):
                if value >= 10:
                    noteCombination[3] += 1
                    value -= 10
                else:
                    break
        if cashier.note5 > 0:
            for i in range(cashier.note5):
                if value >= 5:
                    noteCombination[2] += 1
                    value -= 5
                else:
                    break
        if cashier.note2 > 0:
            for i in range(cashier.note2):
                if value >= 2:
                    noteCombination[1] += 1
                    value -= 2
                else:
                    break
        if cashier.note1 > 0:
            for i in range(cashier.note1):
                if value >= 1:
                    noteCombination[0] += 1
                    value -= 1
                else:
                    break
        if value != 0:
            return 1
        else:
            return noteCombination
    
    def getCombinations(self, value):
        combination = self.combination(value)
        if(combination == 1):
            return None, None, "A quantia de P$" + str(value) + " é muito grande para o estoque atual do caixa..."
        else:
            combinationAlt = self.combinationAlternative(value)
            return combination, combinationAlt, "Escolha uma das combinações"
    
    def post(self, account, withdraw):
        account.balance -= withdraw
        account.save()

class FormTransaction(forms.Form):
    # transaction_transferring_name = forms.CharField(label='Nome do Transferinte', max_length=100)
    transaction_value = forms.DecimalField(label='Valor do saque', max_digits=19, decimal_places=2)
    transaction_benefited_name = forms.CharField(label='Nome do Beneficiado', max_length=100)
    
    def post(self, transferring, data):
        account_transferring = Account.objects.get(id=transferring)
        account_benefited = Account.objects.get(name__iexact=data['transaction_benefited_name'])
        if data['transaction_value'] <= account_transferring.balance:
            account_transferring.balance -= data['transaction_value']
            account_benefited.balance += data['transaction_value']
            account_transferring.save()
            account_benefited.save()

            history = Transaction.objects.create(account_id=account_transferring.id, action='TRANSF.: P$' + str(data['transaction_value']), affected_account_id=account_benefited.id)
            history.save()

class FormCashier(forms.Form):
    cashier_note1 = forms.IntegerField(label='Cédulas de P$1')
    cashier_note2 = forms.IntegerField(label='Cédulas de P$2')
    cashier_note5 = forms.IntegerField(label='Cédulas de P$5')
    cashier_note10 = forms.IntegerField(label='Cédulas de P$10')
    cashier_note20 = forms.IntegerField(label='Cédulas de P$20')
    cashier_note50 = forms.IntegerField(label='Cédulas de P$50')
    cashier_note100 = forms.IntegerField(label='Cédulas de P$100')
    
    def post(self, data):
        cashier = Cashier.objects.get(id=1)
        cashier.note1 = data['cashier_note1']
        cashier.note2 = data['cashier_note2']
        cashier.note5 = data['cashier_note5']
        cashier.note10 = data['cashier_note10']
        cashier.note20 = data['cashier_note20']
        cashier.note50 = data['cashier_note50']
        cashier.note100 = data['cashier_note100']
        cashier.save()