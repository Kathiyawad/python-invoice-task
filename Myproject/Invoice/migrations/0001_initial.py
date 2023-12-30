# Generated by Django 4.2.5 on 2023-09-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('customername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model_Invoice_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('quantity', models.IntegerField(default=True, null=True)),
                ('unitprice', models.IntegerField(default=True, null=True)),
                ('price', models.IntegerField(default=True, null=True)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Invoice.model_invoice')),
            ],
        ),
    ]
