# make sure this is at the top if it isn't already
from django import forms

# our new form
class NameForm(forms.Form):
    card_name = forms.CharField(required=True)
