# Generated by Django 4.0.4 on 2022-06-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coletanea', '0010_alter_item_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categoria',
            field=models.CharField(choices=[('AC', 'Ação'), ('AV', 'Aventura'), ('CM', 'Comédia')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='tipo',
            field=models.CharField(choices=[('F', 'Filme'), ('S', 'Série')], default='', max_length=1),
        ),
    ]