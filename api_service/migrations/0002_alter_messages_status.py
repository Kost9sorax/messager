# Generated by Django 4.0.4 on 2022-05-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='status',
            field=models.CharField(default='review', max_length=255, null=True, verbose_name='Status'),
        ),
    ]
