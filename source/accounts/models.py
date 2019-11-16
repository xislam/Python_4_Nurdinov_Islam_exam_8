from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Token(models.Model):
    token = models.UUIDField(verbose_name='Token', default=uuid4)
    user = models.ForeignKey('auth.User', related_name='registration_tokens',
                             verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.token)


class Url(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accounts_url')
    url = models.URLField(max_length=300, null=True, blank=True, verbose_name='Ссылки на другие информыции о вас ')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return str(self.url)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Url.objects.create(user=instance)


