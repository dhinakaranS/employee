# Generated by Django 2.2.3 on 2019-07-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_ID', models.CharField(max_length=20)),
                ('Emp_Name', models.CharField(max_length=35)),
                ('Designation', models.CharField(max_length=30)),
                ('Salary', models.BigIntegerField()),
            ],
        ),
    ]
