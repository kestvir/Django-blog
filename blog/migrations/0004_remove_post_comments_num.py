# Generated by Django 3.0.6 on 2020-06-04 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200604_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments_num',
        ),
    ]
