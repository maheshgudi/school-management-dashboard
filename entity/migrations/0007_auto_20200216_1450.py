# Generated by Django 3.0.3 on 2020-02-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0006_auto_20200216_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='shape',
            field=models.CharField(choices=[('oval', 'oval'), ('rectangular', 'rectangular'), ('canopy', 'canopy'), ('elevated', 'elevated')], max_length=20),
        ),
    ]
