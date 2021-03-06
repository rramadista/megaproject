# Generated by Django 2.0.7 on 2018-08-04 12:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('benchmark', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('tin', models.CharField(blank=True, max_length=50, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=50, null=True)),
                ('est_date', models.DateField(blank=True, null=True)),
                ('forex_date', models.DateField(blank=True, null=True)),
                ('listing_date', models.DateField(blank=True, null=True)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DimDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('date_as_integer', models.SmallIntegerField()),
                ('month', models.SmallIntegerField()),
                ('month_name', models.CharField(max_length=50)),
                ('quarter', models.SmallIntegerField()),
                ('quarter_name', models.CharField(max_length=10)),
                ('year', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pbt', models.DecimalField(decimal_places=2, max_digits=20)),
                ('asset', models.DecimalField(decimal_places=2, max_digits=20)),
                ('funding', models.DecimalField(decimal_places=2, max_digits=20)),
                ('lending', models.DecimalField(decimal_places=2, max_digits=20)),
                ('pers_exp', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benchmark.Bank')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='benchmark.DimDate')),
            ],
        ),
    ]
