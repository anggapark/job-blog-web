# Generated by Django 3.2.13 on 2022-06-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0007_auto_20220601_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Web Developers', 'Web Developers'), ('Mobile Developers', 'Mobile Developers'), ('UI/UX Designer', 'UI/UX Designer'), ('Machine Learning Engineer', 'Machine Learning Engineer'), ('Data Scientist', 'Data Scientist'), ('Game Developer', 'Game Developer'), ('Security Engineer', 'Security Engineer')], max_length=50),
        ),
    ]
