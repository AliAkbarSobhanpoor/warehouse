# Generated by Django 5.2.3 on 2025-07-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalinvoice',
            name='invoice_type',
            field=models.CharField(choices=[('buy', 'خرید'), ('sell', 'فروش')], default='buy', max_length=10, verbose_name='نوع فاکتور'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('buy', 'خرید'), ('sell', 'فروش')], default='buy', max_length=10, verbose_name='نوع فاکتور'),
        ),
    ]
