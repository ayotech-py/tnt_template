from django.forms import forms
from .models import PropertyModel


class PropertyForm(forms.Form):
    class Meta:
        model = PropertyModel
        fields = "__all__"
