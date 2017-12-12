from django.db import models

class AccountManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(name__icontains=query)

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

class Cashier(models.Model):
    note1 = models.IntegerField('Qtd. de Cédulas de P$1', default=10)
    note2 = models.IntegerField('Qtd. de Cédulas de P$2', default=10)
    note5 = models.IntegerField('Qtd. de Cédulas de P$5', default=10)
    note10 = models.IntegerField('Qtd. de Cédulas de P$10', default=10)
    note20 = models.IntegerField('Qtd. de Cédulas de P$20', default=10)
    note50 = models.IntegerField('Qtd. de Cédulas de P$50', default=10)
    note100 = models.IntegerField('Qtd. de Cédulas de P$100', default=10)