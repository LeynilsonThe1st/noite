from django import forms
from .models import Comentario, ViwerEmail
from django.utils.translation import gettext_lazy as _


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome', 'email', 'conteudo')

        labels = {
            'conteudo': _('Comentario'),
            'email': _('E-mail'),
        }


class SubscreverForm(forms.ModelForm):
    class Meta:
        model = ViwerEmail
        fields = ('email',)
        labels = {
            'email': _('E-mail'),
        }