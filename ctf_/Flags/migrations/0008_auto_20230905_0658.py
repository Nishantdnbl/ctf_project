# Generated by Django 3.2.20 on 2023-09-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flags', '0007_auto_20230829_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit_flag',
            name='flag_1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='submit_flag',
            name='flag_2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='submit_flag',
            name='flag_3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='submit_flag',
            name='flag_4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='submit_flag',
            name='flag_5',
            field=models.CharField(max_length=1000),
        ),
    ]