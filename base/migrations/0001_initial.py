# Generated by Django 4.1.2 on 2022-10-16 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_bio', models.CharField(max_length=500)),
                ('long_bio', models.TextField(blank=True, null=True)),
                ('years_of_exp', models.SmallIntegerField(default=1)),
                ('profile_pic', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('logo', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('sample_photo', models.URLField(unique=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.advocate')),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='likes', to='base.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project')),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_url', models.URLField(unique=True)),
                ('member_since', models.DateTimeField(blank=True, null=True)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('level_of_mastery', models.CharField(blank=True, choices=[('Starter', 'Starter'), ('Basic', 'Basic'), ('Cofortable', 'Cofortable'), ('Skillfull', 'Skillfull'), ('Master', 'Master')], max_length=20, null=True)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company')),
            ],
        ),
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company'),
        ),
    ]
