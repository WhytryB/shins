from django.shortcuts import render
from django.shortcuts import render
from .models import Person
from .forms import UsersForm2, SmsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import uuid

from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


def login(request):
    """
         Функция входа пользователя на сайт
         user_form -  работает из админки и содержит поле username пользвоателя
         sms_form -  Нужна для обработки кода смс
       """

    user_form = UsersForm2()
    sms_form = SmsForm()
    print(1)
    if request.method == "POST":

        user_form = UsersForm2(request.POST)
        sms_form = SmsForm(request.POST)
        print("2")
        print(user_form)
        if user_form.is_valid() and sms_form.is_valid():
            print("3")
            password = sms_form.cleaned_data['sms_mes']
            print(user_form.cleaned_data['username'], "+", sms_form.cleaned_data['sms_mes'])
            # аутентификация пользователя
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=password
            )
            if user is not None:
                # Проверка валидности пользователя
                print("4")
                messages.success(request, "Вы успешно залогинили!")
                auth_login(request, user)
                return redirect('/')

            else:
                print(5)
                messages.error(request, "Вы успешно зerf!")


    return render (request, 'login.html',
                   {"user_form": user_form,
                    "sms_form": sms_form,
                    "id": id})





