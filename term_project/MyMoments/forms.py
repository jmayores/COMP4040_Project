from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    date = forms.DateField
    moment = forms.CharField(widget=forms.Textarea(
        attrs={
            'cols': 120
        }
    ))
    class Meta:
        model = Blog
        fields = [
            'date',
            'moment'
        ]