# Generated by Django 3.2.13 on 2022-06-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0011_alter_post_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(blank=True, default='img/account.svg', null=True, upload_to='logo'),
        ),
    ]
