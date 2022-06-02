# Generated by Django 3.2.13 on 2022-06-02 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0015_alter_post_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'Web Developers'), ('2', 'Mobile Developers'), ('3', 'UI/UX Designer'), ('4', 'Machine Learning Engineer'), ('5', 'Data Scientist'), ('6', 'Game Developer'), ('7', 'Security Engineer')], max_length=50),
        ),
    ]
