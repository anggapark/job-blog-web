# Generated by Django 3.2.13 on 2022-06-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Web Developers', ''), ('Mobile Developers', ''), ('UI/UX Designer', ''), ('Machine Learning Engineer', ''), ('Data Scientist', ''), ('Game Developer', ''), ('Security Engineer', '')], max_length=20),
        ),
    ]