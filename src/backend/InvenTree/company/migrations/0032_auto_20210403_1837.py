# Generated by Django 3.0.7 on 2021-04-03 18:37

import InvenTree.fields
import company.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0031_auto_20210103_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=company.models.rename_company_image, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_customer',
            field=models.BooleanField(default=False, help_text='Do you sell items to this company?', verbose_name='Is customer'),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_manufacturer',
            field=models.BooleanField(default=False, help_text='Does this company manufacture parts?', verbose_name='Is manufacturer'),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_supplier',
            field=models.BooleanField(default=True, help_text='Do you purchase items from this company?', verbose_name='Is supplier'),
        ),
        migrations.AlterField(
            model_name='company',
            name='link',
            field=InvenTree.fields.InvenTreeURLField(blank=True, help_text='Link to external company information', verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='company',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='supplierpart',
            name='base_cost',
            field=models.DecimalField(decimal_places=3, default=0, help_text='Minimum charge (e.g. stocking fee)', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='base cost'),
        ),
        migrations.AlterField(
            model_name='supplierpart',
            name='multiple',
            field=models.PositiveIntegerField(default=1, help_text='Order multiple', validators=[django.core.validators.MinValueValidator(1)], verbose_name='multiple'),
        ),
        migrations.AlterField(
            model_name='supplierpart',
            name='packaging',
            field=models.CharField(blank=True, help_text='Part packaging', max_length=50, null=True, verbose_name='Packaging'),
        ),
        migrations.AlterField(
            model_name='supplierpricebreak',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricebreaks', to='company.SupplierPart', verbose_name='Part'),
        ),
    ]
