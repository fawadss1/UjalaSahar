# Generated by Django 4.1.1 on 2022-09-17 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='Facebook_Link',
            new_name='Facebook_Username',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='Linkedin_Link',
            new_name='Linkedin_Username',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='Twitter_Link',
            new_name='Twitter_Username',
        ),
    ]
