# Generated by Django 4.1.4 on 2022-12-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Provide a name for the product', max_length=100, verbose_name='name'),
        ),
    ]