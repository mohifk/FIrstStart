# Generated by Django 3.2.15 on 2022-10-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='dad', max_length=255),
        ),
    ]