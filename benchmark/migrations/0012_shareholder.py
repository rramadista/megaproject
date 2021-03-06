# Generated by Django 2.0.7 on 2018-09-09 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0011_contact_contact_center'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shareholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shareholder', models.CharField(max_length=50)),
                ('share', models.FloatField()),
                ('category', models.CharField(blank=True, choices=[('1', 'Public'), ('2', 'Individual'), ('3', 'Institution')], max_length=1, null=True)),
                ('is_ultimate', models.BooleanField(default=False, max_length=1)),
                ('ultimate_country_name', models.CharField(max_length=50)),
                ('ultimate_country_id', models.CharField(max_length=2, verbose_name='2 Digit ISO')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benchmark.Bank')),
            ],
        ),
    ]
