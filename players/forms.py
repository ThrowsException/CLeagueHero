from django import forms
from .models import Positions


class PlayerInfo(forms.Form):
    position = forms.ChoiceField(
                                 widget=forms.CheckboxSelectMultiple
                                 (
                                 attrs={'class': 'form-control'}),
                                 choices=(Positions.STATUS_CHOICES

    ))
    # position = forms.ModelMultipleChoiceField(queryset=Positions.STATUS_CHOICES)
