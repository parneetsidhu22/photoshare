# Generated by Django 3.2.4 on 2021-07-21 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0008_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dissabled',
            field=models.BooleanField(default=False),
        ),
    ]