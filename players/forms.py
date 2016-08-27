from django import forms
from .models import Positions

class PlayerInfo(forms.Form):
    position = forms.ChoiceField(
                                 widget=forms.CheckboxSelectMultiple
                                 (

                                 ),
                                 choices=(Positions.STATUS_CHOICES

    ))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    # position = forms.ModelMultipleChoiceField(queryset=Positions.STATUS_CHOICES)
