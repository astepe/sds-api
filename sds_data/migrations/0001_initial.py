# Generated by Django 2.2 on 2019-05-03 16:22

from django.db import migrations, models
import sds_data.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyDataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50, validators=[sds_data.validators.validate_manufacturer])),
                ('product_name', models.CharField(max_length=50)),
                ('product_code', models.CharField(blank=True, max_length=50)),
                ('flash_point_fahrenheit', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('specific_gravity_g_cm3', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('nfpa_fire', models.IntegerField(blank=True, null=True, validators=[sds_data.validators.validate_nfpa_number])),
                ('nfpa_health', models.IntegerField(blank=True, null=True, validators=[sds_data.validators.validate_nfpa_number])),
                ('nfpa_reactivity', models.IntegerField(blank=True, null=True, validators=[sds_data.validators.validate_nfpa_number])),
                ('sara_311', models.CharField(blank=True, max_length=250)),
                ('revision_date', models.DateField(blank=True, null=True)),
                ('physical_state', models.CharField(blank=True, max_length=25)),
                ('cas_number', models.CharField(blank=True, max_length=12, validators=[sds_data.validators.validate_cas_format])),
            ],
        ),
    ]
