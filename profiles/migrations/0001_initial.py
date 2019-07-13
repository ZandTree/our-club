# Generated by Django 2.0.1 on 2019-07-12 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=120)),
                ('last_name', models.CharField(default='', max_length=120)),
                ('age', models.SmallIntegerField(blank=True, null=True)),
                ('location', models.CharField(default='', max_length=120)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=profiles.models.make_avatar)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
