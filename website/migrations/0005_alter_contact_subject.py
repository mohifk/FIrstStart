# Generated by Django 3.2.15 on 2022-10-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]