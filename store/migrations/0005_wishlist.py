# Generated by Django 4.0.4 on 2022-05-19 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_transaction_id_orderitem_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=30, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('wished_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
