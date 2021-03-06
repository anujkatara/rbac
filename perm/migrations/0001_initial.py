# Generated by Django 2.1.5 on 2019-04-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'permissions': (('can_view_odd_ids', 'can_view_odd_ids'), ('can_view_even_ids', 'can_view_even_ids')),
            },
        ),
    ]
