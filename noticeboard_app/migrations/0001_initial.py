# Generated by Django 5.0.1 on 2024-02-27 22:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('other', 'Прочее'), ('tanks', 'Танки'), ('holls', 'Хилы'), ('DD', 'ДД'), ('traders', 'Торговцы'), ('guildmeisters', 'Гилдмастеры'), ('questgivers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], default='other', max_length=20)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024)),
                ('date', models.DateField(auto_now_add=True)),
                ('approved', models.CharField(choices=[('RA', 'requires approval'), ('A', 'approved'), ('NA', 'not approved')], default='RA', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticeboard_app.post')),
            ],
        ),
    ]
