# Generated by Django 2.0.6 on 2018-06-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20180615_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name='due date'),
        ),
    ]
