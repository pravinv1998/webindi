# Generated by Django 3.0.5 on 2020-04-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('days', models.CharField(max_length=365)),
                ('date', models.DateField()),
            ],
        ),
    ]
