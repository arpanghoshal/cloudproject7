# Generated by Django 2.0.7 on 2018-07-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addphotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photosname', models.CharField(max_length=100)),
                ('photosbrowse', models.FileField(upload_to='')),
            ],
        ),
    ]
