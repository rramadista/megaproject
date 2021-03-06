# Generated by Django 2.0.7 on 2018-09-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0012_shareholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareholder',
            name='share',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='ultimate_country_id',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='2 Digit ISO'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='ultimate_country_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
