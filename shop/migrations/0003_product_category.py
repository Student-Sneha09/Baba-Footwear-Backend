# Generated by Django 5.2.4 on 2025-07-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('kid', 'Kid')], default='men', max_length=10),
        ),
    ]
