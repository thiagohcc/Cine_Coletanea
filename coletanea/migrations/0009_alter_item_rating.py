# Generated by Django 4.0.4 on 2022-05-31 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletanea', '0008_alter_item_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rating',
            field=models.CharField(choices=[('0', '☆☆☆☆☆'), ('1', '★☆☆☆☆'), ('2', '★★☆☆☆'), ('3', '★★★☆☆'), ('4', '★★★★☆'), ('5', '★★★★★')], default='0', max_length=1),
        ),
    ]
