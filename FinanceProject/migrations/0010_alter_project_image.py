# Generated by Django 4.0.4 on 2022-04-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceProject', '0009_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='FianceProject/project2.jpg', upload_to='', verbose_name='Image'),
        ),
    ]
