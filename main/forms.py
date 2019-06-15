from django import forms
from login.models import Person
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Shins(forms.Form):
    shine = forms.CharField()
    shirina = forms.CharField()
    profile = forms.CharField()
    radius = forms.CharField()
    brand = forms.CharField()

    god = forms.CharField()
    iznos1 = forms.FloatField()
    iznos2 = forms.FloatField()
    iznos3 = forms.FloatField()
    iznos4 = forms.FloatField()
    latki = forms.CharField()
    sxod = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = Person
        fields = ('shine','shirina','profile','radius','brand','god','iznos1','iznos2','iznos3','iznos4',
                  'latki', 'sxod','first_name',)