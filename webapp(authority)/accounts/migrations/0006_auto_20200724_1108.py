# Generated by Django 2.2 on 2020-07-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200723_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='aadhar',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='city',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=72),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='country',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=72),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='dlicense',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='dob',
            field=models.DateField(error_messages={1: 'Enter Valid Information'}, help_text='Enter in DD/MM/YYYY Format'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(error_messages={1: 'Enter Valid Information'}, max_length=254),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='firstname',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=140),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=7),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='height',
            field=models.IntegerField(error_messages={1: 'Enter Valid Information'}, max_length=3),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='lastname',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=140),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='pancard',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='passport',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='placeOfBirth',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=140),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='prev_records',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='unique_feature',
            field=models.TextField(error_messages={1: 'Enter Valid Information'}, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='zipcode',
            field=models.CharField(error_messages={1: 'Enter Valid Information'}, max_length=10),
        ),
    ]