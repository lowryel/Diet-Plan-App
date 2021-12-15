from django.forms import ModelForm, fields
from .models import fill_formModel

class fill_formForm(ModelForm):
    class Meta:
        model = fill_formModel
        fields=['age', 'weight', 'height', 'weekly_budget']
