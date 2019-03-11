# Generated by Django 2.1.7 on 2019-03-04 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('stage', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Category')),
            ],
        ),
    ]
