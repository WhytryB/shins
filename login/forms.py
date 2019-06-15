from django import forms
from .models import Person
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _





class UsersForm2(forms.Form):
    # Класс формы которая расширяет функционал админки и добавляет поле username
    # на страницу добавления и редактирования персоны, а также изменяет валидацию юзернейма
    username = forms.CharField(label=_(""),
                                error_messages={'invalid': _("Непрвильный никнейм")})
    class Meta:
        model = User
        fields = ('username',)


class SmsForm(forms.Form):
    #  Класс формы, поел которой хранит полученный код , который вводит пользователь при регитсрации или входе.
    sms_mes = forms.CharField(
                              label= "",

                              error_messages={
                                  'invalid': _("Неправильный пароль"),
                                               })

    class Meta:
        model = Person
        fields = ('sms_mes',)


