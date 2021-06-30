from django import forms
from .models import Feed,Gallery,Comment

class FeedForm(forms.ModelForm):
    class Meta:
        model=Feed
        fields=['title','image','video','description']

class GalleryForm(forms.ModelForm):
    gallery=forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=Gallery
        fields=['gallery']
        
