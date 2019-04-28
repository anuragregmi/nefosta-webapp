# Generated by Django 2.2 on 2019-04-28 05:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nefosta', '0006_auto_20190428_0556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('-posted_on',)},
        ),
        migrations.AddField(
            model_name='publication',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]