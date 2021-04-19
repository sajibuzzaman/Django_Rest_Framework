# Generated by Django 3.2 on 2021-04-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0003_shopcart_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='variant',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
