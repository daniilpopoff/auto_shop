from django import forms
from . import models

class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarAnnouncement
        fields = "__all__"

class CarSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)