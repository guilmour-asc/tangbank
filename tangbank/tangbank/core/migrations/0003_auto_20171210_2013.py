# Generated by Django 2.0 on 2017-12-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_transaction_made_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='made_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Feito em...'),
        ),
    ]