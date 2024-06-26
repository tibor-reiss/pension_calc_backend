# Generated by Django 5.0.6 on 2024-06-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PensionCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_contribution', models.DecimalField(decimal_places=2, max_digits=10)),
                ('yearly_interest_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('starting_capital', models.DecimalField(decimal_places=2, max_digits=10)),
                ('term', models.DecimalField(decimal_places=0, max_digits=3)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
