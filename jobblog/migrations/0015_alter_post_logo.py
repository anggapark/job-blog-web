# Generated by Django 3.2.13 on 2022-06-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0014_auto_20220601_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(blank=True, default='account.svg', null=True, upload_to='logo'),
        ),
    ]
