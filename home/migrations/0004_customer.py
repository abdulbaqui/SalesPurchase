# Generated by Django 3.0.6 on 2020-06-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_sales_data_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_ID', models.IntegerField(max_length=2000)),
                ('Customer_Name', models.CharField(max_length=150)),
                ('Status', models.BooleanField()),
            ],
        ),
    ]
