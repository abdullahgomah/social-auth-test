# Generated by Django 4.1.4 on 2022-12-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(default=111, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.TextField(max_length=100),
        ),
    ]
