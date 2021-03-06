# Generated by Django 2.0.7 on 2018-09-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0014_auto_20180911_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(max_length=50, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='est_date',
            field=models.DateField(blank=True, null=True, verbose_name='Establishment Date'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='forex_date',
            field=models.DateField(blank=True, null=True, verbose_name='Foreign Exchange Operations Date'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='institution_name',
            field=models.CharField(max_length=100, verbose_name='Institution Name'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='listing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Listing Date'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='periods',
            field=models.ManyToManyField(through='benchmark.Indicator', to='benchmark.DimDate'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='tin',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tax Identification Number'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='headcount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
