# Generated by Django 5.0.3 on 2024-03-10 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0005_moviecomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecomment',
            old_name='text',
            new_name='comment',
        ),
    ]