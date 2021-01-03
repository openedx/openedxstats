# Generated by Django 2.2.17 on 2021-01-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0012_site_is_gone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geozone',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.AddIndex(
            model_name='site',
            index=models.Index(fields=['active_end_date'], name='sites_site_active__0269fd_idx'),
        ),
    ]