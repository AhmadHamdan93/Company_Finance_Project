# Generated by Django 4.0.4 on 2022-04-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceProject', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/images/project1.jpg', upload_to='', verbose_name='Image'),
        ),
    ]