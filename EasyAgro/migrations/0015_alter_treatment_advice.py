# Generated by Django 4.0.4 on 2023-05-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyAgro', '0014_postplantingprocess_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='advice',
            field=models.CharField(max_length=600),
        ),
    ]
