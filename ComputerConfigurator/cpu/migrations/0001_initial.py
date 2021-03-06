# Generated by Django 3.0.7 on 2020-07-19 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=256)),
                ('model', models.TextField(max_length=256)),
                ('kernel', models.PositiveIntegerField()),
                ('speed', models.FloatField()),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
