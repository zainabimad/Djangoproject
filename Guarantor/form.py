from django import forms
from .models import AddGu


class AddFormG(forms.ModelForm):
    class Meta:
        model = AddGu
        fields = "__all__"

