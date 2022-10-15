# Generated by Django 4.1.2 on 2022-10-15 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_advocate_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('sample_photo', models.ImageField(blank=True, null=True, upload_to='project/sample')),
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
    ]
