from django import forms


class ProfileSearchForm(forms.Form):
    battle_tag = forms.CharField(max_length=100, required=True)
