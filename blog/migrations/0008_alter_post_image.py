# Generated by Django 3.2.15 on 2022-10-09 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defult.jpg', upload_to='media/blog/'),
        ),
    ]
