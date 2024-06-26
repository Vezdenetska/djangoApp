# Generated by Django 5.0.3 on 2024-03-31 17:29

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Tytuł artykułu')),
                ('text', models.TextField(verbose_name='Tekst artykułu')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data:')),
                ('views', models.IntegerField(default=1, verbose_name='Wyświetlenia:')),
                ('avtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor:')),
            ],
            options={
                'verbose_name': 'Wiadomość',
                'verbose_name_plural': 'Wiadomości',
            },
        ),
    ]
