# Generated by Django 3.2.20 on 2023-08-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('flag1', models.IntegerField()),
                ('flag2', models.IntegerField()),
                ('flag3', models.IntegerField()),
                ('flag4', models.IntegerField()),
                ('flag5', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
