# Generated by Django 3.2.13 on 2022-06-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobblog', '0013_alter_post_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='job_type',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.CharField(max_length=200),
        ),
    ]
