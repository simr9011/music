# Generated by Django 3.0.8 on 2020-08-01 09:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Album title', max_length=100)),
                ('artist', models.CharField(help_text='Album artist', max_length=100)),
                ('genre', models.CharField(help_text='Album genre', max_length=50)),
                ('year', models.DateField(help_text='Album year')),
                ('image', models.FileField(default='', upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])])),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Songs title', max_length=100)),
                ('artist', models.CharField(help_text='Song artist', max_length=100)),
                ('genre', models.CharField(help_text='Song genre', max_length=50)),
                ('image', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])])),
                ('soundfile', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3', 'aac'])])),
                ('al_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmusic.Album')),
            ],
        ),
    ]
