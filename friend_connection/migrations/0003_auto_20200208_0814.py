# Generated by Django 3.0.3 on 2020-02-08 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend_connection', '0002_auto_20200208_0705'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='friends',
            name='friend1_friend2_unique_constraint',
        ),
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together={('friend1', 'friend2')},
        ),
    ]
