# Generated by Django 2.2 on 2019-04-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='zip',
            field=models.CharField(max_length=10),
        ),
    ]
