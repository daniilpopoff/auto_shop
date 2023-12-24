from django import forms
from . import models

class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarAnnouncement
        fields = ['name_car', 'image', 'price_usd', 'price_soms', 'year', 'mileage', 'body_type', 'color', 'engine',
                  'transmission', 'drive', 'steering_left', 'condition', 'customs_clearance', 'exchange_offer',
                  'availability', 'region_city', 'country', 'category']


class CarSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)