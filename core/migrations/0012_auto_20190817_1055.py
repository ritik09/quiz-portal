# Generated by Django 2.0.6 on 2019-08-17 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190817_1043'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categorymarks',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='categorymarks',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='categorymarks',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categorymarks',
            name='test',
        ),
        migrations.DeleteModel(
            name='CategoryMarks',
        ),
    ]
