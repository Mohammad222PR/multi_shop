# Generated by Django 4.2.3 on 2023-07-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_otp_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
