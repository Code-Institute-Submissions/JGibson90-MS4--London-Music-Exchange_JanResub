# Generated by Django 3.2.6 on 2021-09-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210922_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orginal_bag',
            new_name='original_bag',
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]