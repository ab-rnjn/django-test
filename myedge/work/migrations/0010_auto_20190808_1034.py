# Generated by Django 2.2.2 on 2019-08-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_auto_20190718_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_title', models.CharField(default=None, max_length=100)),
                ('mission_text', models.TextField(default='')),
                ('vision_title', models.CharField(default=None, max_length=100)),
                ('vision_text', models.TextField(default='')),
                ('history_title', models.CharField(default=None, max_length=100)),
                ('history_text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(default=None, max_length=100)),
                ('news_image', models.ImageField(upload_to='media')),
                ('news_text', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='campaign_date',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='gallery',
            name='award_image',
            field=models.ImageField(default=' ', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='award_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='gallery',
            name='award_time',
            field=models.DateField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='gallery_title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='gallery',
            name='video_title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='upcoming_events',
            name='event_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='upcoming_events',
            name='event_title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
