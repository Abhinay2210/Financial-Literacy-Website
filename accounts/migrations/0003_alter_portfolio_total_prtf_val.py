# Generated by Django 3.2.5 on 2021-11-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211007_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='total_prtf_val',
            field=models.IntegerField(default=0),
        ),
    ]
