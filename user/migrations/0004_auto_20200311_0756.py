# Generated by Django 3.0.3 on 2020-03-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200310_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]