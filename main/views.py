from django.shortcuts import render
from .forms import *
from login.models import *
from login.forms import *
# Create your views here.
from django.views.generic import View
import csv
import re

userna = "Ещё нет"

class MainView(View):
    template = 'main.html'

    def get(self, request):
        global userna
        form = Shins()
        try:
            person = Person.objects.get(first_name=userna[0], second_name=userna[1],
                                        third_name=userna[2])


            if 'yes' in request.GET:

                person.soglas = "Да"

            elif 'no' in request.GET:

                person.soglas = "Нет"
            person.save()
        except Exception:
            pass
        try:
            a = Company.objects.get(users__username=request.user)
            a = a.person.all()
        except Exception:
            a = ""
        return render(request, self.template,
                      context={"form": form, "b":a})



    def post(self, request):
        global userna
        form = Shins(request.POST)
        user_form = UsersForm2(request.POST)
        if form.is_valid():
            shine = form.cleaned_data['shine']
            shirina = form.cleaned_data['shirina']
            profile = form.cleaned_data['profile']
            radius = form.cleaned_data['radius']
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            god = form.cleaned_data['god']
            iznos1 = form.cleaned_data['iznos1']
            iznos2 = form.cleaned_data['iznos2']
            iznos3 = form.cleaned_data['iznos3']
            iznos4 = form.cleaned_data['iznos4']
            latki = form.cleaned_data['latki']
            first_name = form.cleaned_data['first_name']

            left_colum = shirina + "/" + profile + "/" + radius
            print(left_colum)
            premium = ['Pirelli', 'Continental', 'Michelin', 'Nokian', 'Toyo', 'Yokohama', 'Dunlop', 'Bridgestone',
                       'Goodyear', 'Aston Martin']

            standard = ['Kumho', 'Hankook', 'Nexen', 'Gislaved', 'Firestone', 'BFGoodrich', 'Matador', 'Barum',
                        'Falken', 'Viatti', 'Tigar', 'Barum','Alfa Romeo',]

            brand_wo = "Д"
            if brand in premium:
                brand_wo = "П"
            elif brand in standard:
                brand_wo = "С"

            iznos = (int(iznos1) + int(iznos2) + int(iznos3) + int(iznos4))
            iznos_wo = ""
            if shine == "Шины, летние":
                iznos = iznos/8
            elif shine == "Шины, зимние шипованные" or shine == "Шины, зимние нешипованные":
                iznos = iznos/10

            if iznos >= 0 and iznos<= 15:
                iznos_wo = "П"
            elif iznos > 15 and iznos <= 30:
                iznos_wo = "Н"
            else:
                iznos_wo = "У"

            god_wo = ""
            god_raz = (2019 - int(god))
            if god_raz <= 3:
                god_wo = "М"
            elif god_raz <8:
                god_wo = "С"
            else:
                god_wo = "Д"

            right_column = brand_wo + '/' + iznos_wo + '/' + god_wo
            print(right_column)
            file_obj = open("main/Estimation.csv")
            reader = csv.DictReader(file_obj, delimiter=',')
            spisok = {}
            for line in reader:
                d = {line["Размер"]:line[right_column]}
                spisok.update(d)

            cena = spisok.get(left_colum)
            print(cena)
            if cena == None:
                cena = "Не правильно выбранны параметры"
                hide = False
            else:
                hide = True

            if latki == "Yes":
                latki = "Да"
                try:
                    skidka = (int(cena) * 0.1)
                    cena = int(cena) - int(skidka)
                except Exception:
                    skidka = 0
            else:
                latki = "Нет"
                skidka = 0


            # СОхранение номера телефона пользователя в модели
            print(first_name, "-------")

            fio = re.findall(r"[\w']+", first_name)

            person = Person.objects.get(first_name=fio[0],second_name=fio[1],
                                        third_name=fio[2])
            person.shine = shine
            person.shirina = shirina
            person.profile = profile
            person.radius = radius
            person.brand = brand
            person.model = model
            person.god = god
            person.iznos1 = iznos1
            person.iznos2 = iznos2
            person.iznos3 = iznos3
            person.iznos4 = iznos4
            person.latki = latki
            person.cena = cena
            person.iznos = iznos
            person.skidka = skidka
            person.save()
            userna = fio


            a = Company.objects.get(users__username=request.user)
            a = a.person.all()

            return render(request, self.template, context={'form': form, "cena":cena, "iznos":iznos, "latki":latki,
                                                           "skidka":skidka, "hide":hide, "b": a})