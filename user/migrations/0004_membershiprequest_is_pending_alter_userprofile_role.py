# Generated by Django 5.0.1 on 2024-03-04 04:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_role_alter_userprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiprequest',
            name='is_pending',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.role'),
        ),
    ]
