from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse




class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name




class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Car(Product):
    marka = models.CharField(max_length=255, verbose_name='Марка')
    engine = models.CharField(max_length=255, verbose_name='Двигатель')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    year = models.CharField(max_length=255, verbose_name='Год')





class Notebook(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип доступа')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процесора')
    ram = models.CharField(max_length=255, verbose_name='Оперитавная память')
    video = models.CharField(max_length=255, verbose_name='Видео карта')
    time_without_change = models.CharField(max_length=255, verbose_name='Время работы акумулятора')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)






class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип доступа')
    resolution = models.CharField(max_length=255, verbose_name='Разрние экрана')
    accum_volume = models.CharField(max_length=255, verbose_name='Обьем батареии')
    ram = models.CharField(max_length=255, verbose_name='Оперитавная память')
    main_camp_mp = models.CharField(max_length=255, verbose_name='Главная камера')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная камера')

    def __str__(self):
        return "{}: {}".format(self.category.name, self.title)





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=255, verbose_name='Телефон номер')




