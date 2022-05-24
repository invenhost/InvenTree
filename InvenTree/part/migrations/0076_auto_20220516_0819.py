# Generated by Django 3.2.13 on 2022-05-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0075_auto_20211128_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='metadata',
            field=models.JSONField(blank=True, help_text='JSON metadata field, for use by external plugins', null=True, verbose_name='Plugin Metadata'),
        ),
        migrations.AddField(
            model_name='partcategory',
            name='metadata',
            field=models.JSONField(blank=True, help_text='JSON metadata field, for use by external plugins', null=True, verbose_name='Plugin Metadata'),
        ),
    ]