# Generated by Django 4.1.2 on 2022-10-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialaccount',
            old_name='account_on',
            new_name='account_url',
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]