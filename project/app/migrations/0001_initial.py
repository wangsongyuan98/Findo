# Generated by Django 3.0.5 on 2020-11-28 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_id', models.IntegerField(default=0)),
                ('product_name', models.CharField(default='unnamed', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.IntegerField(default=0)),
                ('company_name', models.CharField(max_length=50)),
                ('date', models.CharField(default='unknown', max_length=50)),
                ('price', models.DecimalField(decimal_places=50, default=0, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StructuredFinancialInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SFI_id', models.IntegerField(default=0)),
                ('Knock_in', models.DecimalField(decimal_places=50, default=0, max_digits=100)),
                ('Knock_out', models.DecimalField(decimal_places=50, default=0, max_digits=100)),
                ('put_strike', models.DecimalField(decimal_places=50, default=0, max_digits=100)),
                ('fp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FinancialProduct')),
                ('stock_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StockInfo')),
            ],
        ),
    ]