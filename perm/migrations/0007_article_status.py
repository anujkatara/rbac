# Generated by Django 2.1.5 on 2019-05-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perm', '0006_auto_20190412_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('InProgress', 'InProgress'), ('approved', 'Approved')], default='pending', max_length=10),
        ),
    ]
