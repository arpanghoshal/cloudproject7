# Generated by Django 2.0.7 on 2018-07-10 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]