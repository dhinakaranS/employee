# Generated by Django 2.2.3 on 2019-07-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp', '0002_remove_employee_emp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Designation',
            new_name='DESIGNATION',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Emp_Name',
            new_name='NAME',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Salary',
            new_name='SALARY',
        ),
        migrations.AddField(
            model_name='employee',
            name='STATUS',
            field=models.CharField(choices=[('1', 'Current'), ('0', 'Releaved')], default='1', max_length=2),
        ),
    ]
