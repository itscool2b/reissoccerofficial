# Generated by Django 4.1.12 on 2023-11-15 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_dashboardstats_user_alter_player_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardstats',
            name='total_blue_cards',
        ),
    ]
