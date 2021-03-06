from django import forms
from django.forms.extras.widgets import Select


class RatingForm(forms.Form):
    ice_surface = forms.ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=(
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ))
    referees = forms.ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=(
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ))
    lockers = forms.ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=(
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ))
    league = forms.ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=(
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ))
    teams = forms.ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=(
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class SearchForm(forms.Form):
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    within = forms.ChoiceField(widget=Select(attrs={'class': 'form-control'}),
                               choices=(
                                         (5, '5 miles'),
                                         (10, '10 miles'),
                                         (25, '25 miles'),
                                         (100, '100 miles')
                                        ))
    lng = forms.CharField(widget=forms.HiddenInput())
    lat = forms.CharField(widget=forms.HiddenInput())
