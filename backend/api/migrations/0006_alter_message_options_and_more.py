# Generated by Django 5.2 on 2025-05-05 23:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_resource'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['timestamp']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='message',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='message',
            name='parent_message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
