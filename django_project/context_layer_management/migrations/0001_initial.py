# Generated by Django 4.2.7 on 2024-05-20 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of data.', max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('source', models.CharField(blank=True, help_text='Source of resource.', max_length=512, null=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('fields', models.JSONField(blank=True, default=list, null=True)),
                ('is_ready', models.BooleanField(default=False, help_text='Indicates if the layer has been ready.')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.CharField(choices=[('Vector Tile', 'Vector Tile'), ('Raster Tile', 'Raster Tile')], default='Vector Tile', max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]