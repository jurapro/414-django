from audioop import reverse

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    USERNAME_FIELD = 'username'

    def full_name(self):
        # return self.name + ' ' + self.surname + ' ' + self.patronymic
        return ' '.join([self.name, self.surname, self.patronymic])

    def __str__(self):
        return self.full_name()


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class Product(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    photo_file = models.ImageField(max_length=254, upload_to=get_name_file,
                                   blank=True, null=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    year = models.IntegerField(verbose_name='Год производства', blank=True)
    country = models.CharField(max_length=254, verbose_name='Страна производства', blank=True)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, blank=False,
                                default=0.00)
    count = models.IntegerField(verbose_name='Количество', blank=False, default=1)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Наименование', blank=False)

    def __str__(self):
        return self.name