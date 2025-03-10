# Generated by Django 4.2.19 on 2025-02-25 22:14

import common.icons
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0113_stockitem_status_custom_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stocklocation",
            name="custom_icon",
            field=models.CharField(
                blank=True,
                db_column="icon",
                help_text="Icon (optional)",
                max_length=100,
                null=True,
                validators=[common.icons.validate_icon],
                verbose_name="Icon",
            ),
        ),
    ]
