# Generated by Django 4.2.12 on 2024-06-09 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0050_auto_20240508_0138'),
        ('common', '0026_auto_20240608_1238'),
        ('company', '0069_company_active'),
        ('order', '0099_alter_salesorder_status'),
        ('part', '0123_parttesttemplate_choices'),
        ('stock', '0110_alter_stockitemtestresult_finished_datetime_and_more')
    ]

    operations = [
        migrations.DeleteModel(
            name='PartAttachment',
        ),
    ]
