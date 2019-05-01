# Generated by Django 2.2 on 2019-05-01 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nefosta', '0009_auto_20190428_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ('-posted_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DownloadResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('_url', models.URLField(blank=True, verbose_name='URL')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloads', to='nefosta.DownloadCategory')),
            ],
            options={
                'ordering': ('-posted_on',),
                'abstract': False,
            },
        ),
    ]
