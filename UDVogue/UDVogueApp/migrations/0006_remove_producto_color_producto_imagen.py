# Generated by Django 5.1.3 on 2024-12-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UDVogueApp', '0005_revista_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='color',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos/'),
        ),
    ]
