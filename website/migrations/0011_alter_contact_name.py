# Generated by Django 3.2.15 on 2022-10-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]