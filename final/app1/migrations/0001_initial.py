# Generated by Django 3.0.1 on 2019-12-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(auto_created=True)),
                ('text', models.CharField(max_length=200)),
                ('message', models.FileField(upload_to='musics/')),
            ],
        ),
    ]
