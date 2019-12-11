# Generated by Django 2.2 on 2019-11-16 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=300, null=True, verbose_name='Профиль GitHup')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='описание')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accounts_url', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, verbose_name='Token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_tokens', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]