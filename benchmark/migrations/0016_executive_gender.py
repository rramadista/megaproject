# Generated by Django 2.0.7 on 2018-09-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0015_auto_20180913_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]