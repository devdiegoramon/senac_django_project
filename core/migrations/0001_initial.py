# Generated by Django 5.1.3 on 2024-12-01 21:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Financas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renda_mensal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gastos_fixos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gastos_variaveis', models.DecimalField(decimal_places=2, max_digits=10)),
                ('investimentos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dividas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('objetivo_financeiro', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
