# Generated by Django 4.0.6 on 2022-08-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0006_alter_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='BirthDate',
            field=models.DateField(auto_created=True, blank=True),
        ),
    ]