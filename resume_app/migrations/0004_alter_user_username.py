# Generated by Django 4.0.6 on 2022-08-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0003_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserName',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
