# Generated by Django 3.0.3 on 2020-02-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_auto_20200215_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
