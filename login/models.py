from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class Person(models.Model):
    #  Класс моделей в таблице для пользователя
    #  поле телефона пользователя называется - users, оно связанно с стандартным классом пользователя
    first_name = models.CharField('Имя', max_length=100, null=True, blank=False)
    second_name = models.CharField('Фамилия', max_length=100, null=True, blank=False)
    third_name = models.CharField('Отчество', max_length=100, null=True, blank=False)
    shine = models.CharField("Шины",max_length=100, null=True, blank=False)
    shirina = models.CharField("Ширина", max_length=100, null=True, blank=False)
    profile = models.CharField("Профиль", max_length=100, null=True, blank=False)
    radius = models.CharField("Радиус", max_length=100, null=True, blank=False)
    brand = models.CharField("Бренд", max_length=100, null=True, blank=False)
    model = models.CharField("Модель", max_length=100, null=True, blank=False)
    god = models.CharField("Год выпуска", max_length=100, null=True, blank=False)
    iznos1 = models.IntegerField("Износ 1", null=True, blank=False)
    iznos2 = models.IntegerField("Износ 2", null=True, blank=False)
    iznos3 = models.IntegerField("Износ 3",  null=True, blank=False)
    iznos4 = models.IntegerField("Износ 4", null=True, blank=False)
    latki = models.CharField("Есть ли латки", max_length=100, null=True, blank=False)
    soglas = models.CharField("Согласен ли клиент", max_length=100, null=True, blank=False)
    cena  = models.CharField("Общая цена", max_length=100, null=True, blank=False)
    iznos = models.CharField("Общий износ", max_length=100, null=True, blank=False)
    skidka = models.CharField("Скидка", max_length=100, null=True, blank=False)

    def get_fio(self):
        return self.first_name + self.second_name + self.third_name
    #  поле для храненения смс пароля пользователя

    def __str__(self):
        return self.first_name +' '+ self.second_name + ' ' + self.third_name

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'все сотрудники'


class Company(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personshop', null=True)
    person = models.ManyToManyField(Person)
    name = models.CharField("Название компании", max_length=100, null=True, blank=False)


    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'