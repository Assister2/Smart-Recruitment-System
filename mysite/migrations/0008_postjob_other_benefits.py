# Generated by Django 3.2 on 2021-06-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20210609_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='other_benefits',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
