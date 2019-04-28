# Generated by Django 2.2 on 2019-04-28 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nefosta', '0008_link_linkcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='nefosta.LinkCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='link',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
