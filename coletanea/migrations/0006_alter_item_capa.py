# Generated by Django 4.0.4 on 2022-05-01 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletanea', '0005_item_capa_delete_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
