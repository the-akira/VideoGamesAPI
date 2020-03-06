# Generated by Django 3.0.3 on 2020-03-05 21:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular genre', primary_key=True, serialize=False),
        ),
    ]