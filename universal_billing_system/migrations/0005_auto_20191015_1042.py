# Generated by Django 2.0.3 on 2019-10-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universal_billing_system', '0004_auto_20191015_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
