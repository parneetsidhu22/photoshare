# Generated by Django 3.2.4 on 2021-07-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='following',
            new_name='follower',
        ),
    ]
