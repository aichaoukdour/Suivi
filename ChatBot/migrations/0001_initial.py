# Generated by Django 5.1.7 on 2025-05-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('ip_address', models.CharField(max_length=45)),
                ('success', models.BooleanField()),
                ('user_agent', models.TextField()),
                ('date_l', models.DateTimeField()),
            ],
        ),
    ]
