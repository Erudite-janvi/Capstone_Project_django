# Generated by Django 4.2.11 on 2024-03-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.CharField(default='', max_length=13),
        ),
    ]
