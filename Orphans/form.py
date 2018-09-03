from django import forms
from .models import AddOr
from .models import AddRe


class AddForm(forms.ModelForm):
    class Meta:
        model = AddOr
        fields = "__all__"


class AddFormRe(forms.ModelForm):
    class Meta:
        model = AddRe
        fields = "__all__"
