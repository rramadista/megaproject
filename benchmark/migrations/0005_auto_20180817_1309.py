# Generated by Django 2.0.7 on 2018-08-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0004_auto_20180817_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='category',
            field=models.CharField(choices=[('1', 'Stated Owned Bank'), ('2', 'Regional Bank'), ('3', 'Private Forex Bank'), ('4', 'Private Non-Forex Bank'), ('5', 'Joint Venture Bank'), ('6', 'Foreign Bank')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bank',
            name='group',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]