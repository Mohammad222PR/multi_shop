# Generated by Django 4.2.3 on 2023-07-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='text',
            field=models.TextField(blank=True, max_length=100000000000000000, null=True),
        ),
    ]
