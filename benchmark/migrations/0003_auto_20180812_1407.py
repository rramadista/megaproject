# Generated by Django 2.0.7 on 2018-08-12 07:07

from decimal import Decimal
from django.db import migrations, models
import django.utils.timezone
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0002_auto_20180804_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dimdate',
            old_name='month',
            new_name='calendar_quarter',
        ),
        migrations.RenameField(
            model_name='dimdate',
            old_name='quarter',
            new_name='calendar_year',
        ),
        migrations.RenameField(
            model_name='dimdate',
            old_name='year',
            new_name='day_of_month',
        ),
        migrations.RemoveField(
            model_name='dimdate',
            name='date',
        ),
        migrations.RemoveField(
            model_name='dimdate',
            name='date_as_integer',
        ),
        migrations.RemoveField(
            model_name='dimdate',
            name='quarter_name',
        ),
        migrations.RemoveField(
            model_name='financial',
            name='pers_exp',
        ),
        migrations.AddField(
            model_name='dimdate',
            name='calendar_year_month',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='calendar_year_qtr',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='date_name',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='date_name_eu',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='date_name_us',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='day_name_of_week',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='day_of_week',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='day_of_year',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='fiscal_month_of_year',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='fiscal_quarter',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='fiscal_year',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='fiscal_year_month',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='fiscal_year_qtr',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='full_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='dimdate',
            name='is_last_day_of_month',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='month_of_year',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='week_of_year',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimdate',
            name='weekday_weekend',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financial',
            name='asset_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('IDR', 'Indonesian Rupiah'), ('USD', 'US Dollar')], default='IDR', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='financial',
            name='funding_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('IDR', 'Indonesian Rupiah'), ('USD', 'US Dollar')], default='IDR', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='financial',
            name='lending_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('IDR', 'Indonesian Rupiah'), ('USD', 'US Dollar')], default='IDR', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='financial',
            name='pbt_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('IDR', 'Indonesian Rupiah'), ('USD', 'US Dollar')], default='IDR', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bank',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dimdate',
            name='month_name',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='financial',
            name='asset',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='IDR', max_digits=19),
        ),
        migrations.AlterField(
            model_name='financial',
            name='funding',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='IDR', max_digits=19),
        ),
        migrations.AlterField(
            model_name='financial',
            name='lending',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='IDR', max_digits=19),
        ),
        migrations.AlterField(
            model_name='financial',
            name='pbt',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0'), default_currency='IDR', max_digits=19),
        ),
    ]
