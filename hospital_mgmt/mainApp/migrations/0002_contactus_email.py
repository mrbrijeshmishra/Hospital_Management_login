# Generated by Django 4.2.4 on 2023-10-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='heya@gmail.com', max_length=254),
        ),
    ]
