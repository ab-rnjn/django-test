# Generated by Django 2.2.2 on 2019-07-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_auto_20190718_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcoming_events',
            name='event_images',
            field=models.ImageField(upload_to='media'),
        ),
    ]