# Generated by Django 3.0.3 on 2020-07-29 08:00

from django.db import migrations, models
import software.models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0005_auto_20200720_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='image',
            field=models.ImageField(null=True, upload_to=software.models.recipe_image_file_path),
        ),
    ]
