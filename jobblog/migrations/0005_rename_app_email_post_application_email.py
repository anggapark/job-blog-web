# Generated by Django 3.2.13 on 2022-06-01 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0004_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='app_email',
            new_name='application_email',
        ),
    ]
