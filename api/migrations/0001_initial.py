# Generated by Django 3.0.7 on 2021-04-15 13:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
                ('zipcode', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['store_number'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_number', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('cell_phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rx_number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('dosage', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('refill', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prescription_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=50)),
                ('pickup_date', models.DateField(blank=True, null=True)),
                ('update_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
        ),
    ]
