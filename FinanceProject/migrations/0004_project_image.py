# Generated by Django 4.0.4 on 2022-04-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceProject', '0003_alter_expenses_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='some info about project', upload_to='', verbose_name='Image'),
        ),
    ]