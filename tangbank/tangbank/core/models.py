from django.db import models

class AccountManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(name__icontains=query)

    def postWithdraw(self, account_id, value):
        account = Account.objects.get(id=account_id)
        account.balance -= value
        account.save()

class TransactionManager(models.Manager):
    def postWithdraw(self, account_id, value):
        history = Transaction.objects.create(account_id=account_id, action='SAQUE.: P$' + str(value), affected_account_id=account_id)
        history.save()

class CashierManager(models.Manager):
    def postWithdraw(self, comb):
        cashier = Cashier.objects.get(id=1)
        cashier.note1 = comb[0]
        cashier.note2 = comb[1]
        cashier.note5 = comb[2]
        cashier.note10 = comb[3]
        cashier.note20 = comb[4]
        cashier.note50 = comb[5]
        cashier.note100 = comb[6]
        cashier.save()

class Account(models.Model):
    name = models.CharField('Nome', max_length=100)
    balance = models.DecimalField('Saldo', max_digits=19, decimal_places=2)
    objects = AccountManager()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

class Transaction(models.Model):
    account_id = models.IntegerField('ID da Conta')
    action = models.CharField('Ação', max_length=150)
    affected_account_id = models.IntegerField('ID da Conta Afetada')
    made_at = models.DateTimeField('Feito em...', auto_now_add=True)
    objects = TransactionManager()

class Cashier(models.Model):
    note1 = models.IntegerField('Qtd. de Cédulas de P$1', default=10)
    note2 = models.IntegerField('Qtd. de Cédulas de P$2', default=10)
    note5 = models.IntegerField('Qtd. de Cédulas de P$5', default=10)
    note10 = models.IntegerField('Qtd. de Cédulas de P$10', default=10)
    note20 = models.IntegerField('Qtd. de Cédulas de P$20', default=10)
    note50 = models.IntegerField('Qtd. de Cédulas de P$50', default=10)
    note100 = models.IntegerField('Qtd. de Cédulas de P$100', default=10)
    objects = CashierManager()