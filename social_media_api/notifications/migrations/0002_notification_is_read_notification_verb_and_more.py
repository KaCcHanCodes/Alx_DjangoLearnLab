# Generated by Django 5.1.1 on 2024-09-21 22:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notifications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='verb',
            field=models.CharField(choices=[('Like', 'notification on new post like'), ('Follow', 'notification on new following'), ('Comment', 'notifications on post comments'), ('Post', 'notifications on new post')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='object_id',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notif_receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
