# Generated by Django 4.2.3 on 2023-07-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(choices=[('poshak', 'پوشاک'), ('electice', 'دوربین'), ('barghi', 'موبایل'), ('cafsh', 'کفش'), ('abajor', 'ابازور'), ('kerem', 'کرم'), ('saat', 'ساعت'), ('pahbad', 'پهباد')], default='poshak', max_length=200),
        ),
    ]
