from django import forms
from .models import AddAc


class AddFormAc(forms.ModelForm):
    class Meta:
        model = AddAc
        fields = "__all__"

