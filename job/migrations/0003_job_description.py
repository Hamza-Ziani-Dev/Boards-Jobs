# Generated by Django 4.1.5 on 2023-01-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
