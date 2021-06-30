from django import forms
from .models import Status

class StatusForm(forms.Form):
    class Meta:
        fields=['caption','image','video']