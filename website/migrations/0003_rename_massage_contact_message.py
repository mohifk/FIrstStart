# Generated by Django 3.2.15 on 2022-10-16 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]
