# Generated by Django 4.1.1 on 2022-09-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='olimp',
            name='tegs',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]