# Generated by Django 5.0.6 on 2024-11-03 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('superadmin', models.BooleanField(default=False)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.CharField(max_length=100)),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featurename', models.CharField(max_length=100)),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=1000)),
                ('capacity', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('ac_nonac_both', models.CharField(max_length=100)),
                ('ac_rent', models.CharField(max_length=100)),
                ('non_ac_rent', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('images', models.CharField(max_length=100)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
                ('addedby', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
                ('terms', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('total_amount', models.CharField(max_length=100)),
                ('cashreceived', models.CharField(max_length=100)),
                ('remaining_amount', models.CharField(max_length=100)),
                ('booking_id', models.IntegerField()),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday', models.IntegerField(default=0)),
                ('monday', models.IntegerField(default=0)),
                ('tuesday', models.IntegerField(default=0)),
                ('wednesday', models.IntegerField(default=0)),
                ('thursday', models.IntegerField(default=0)),
                ('friday', models.IntegerField(default=0)),
                ('saturday', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
                ('addedby', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhall.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Hallfeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=100)),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhall.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Imagegallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hall_images/')),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhall.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Inoperability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('addedby', models.IntegerField(default=0)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('isdelete', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhall.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeslot', models.CharField(max_length=100)),
                ('ac', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('addedon', models.DateField(auto_now_add=True)),
                ('approval_status', models.IntegerField(default=0)),
                ('evening_before', models.CharField(default='no', max_length=3, null=True)),
                ('features', models.TextField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhall.hall')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhall.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('is_verified', models.BooleanField()),
                ('addedon', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminhall.user')),
            ],
        ),
    ]
