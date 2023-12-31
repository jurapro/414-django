# Generated by Django 4.2.6 on 2023-10-21 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('confirmed', 'Подтвержденный'), ('canceled', 'Отмененный')], default='new', max_length=254, verbose_name='Статус')),
                ('rejection_reason', models.TextField(blank=True, verbose_name='Причина отказа')),
                ('products', models.ManyToManyField(related_name='orders', through='demo.ItemInOrder', to='demo.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='iteminorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='iteminorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.product', verbose_name='Товар'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
