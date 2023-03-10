# Generated by Django 3.2.16 on 2022-12-17 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221217_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='base.reviews')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='base.titles')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментрарии',
            },
        ),
    ]
