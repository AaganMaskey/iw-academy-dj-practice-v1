# Generated by Django 3.0.7 on 2020-07-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('long', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=False)),
                ('country', models.CharField(choices=[('NEPAL', 'NEPAL')], max_length=100)),
                ('bio', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]