from django import forms
from .models import RadioModel

SPAM_CHOICES = [
    ('100', '100'),
    ('300', '300'),
    ('500', '500'),
    ('800', '800'),
    ('1000', '1000')
]


class RadioModelForm(forms.ModelForm):
    spam = forms.ChoiceField(choices=SPAM_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = RadioModel
        fields = ['spam']
