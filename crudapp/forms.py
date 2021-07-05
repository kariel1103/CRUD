from django import forms
from .models import Crud

class PostForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['title', 'body', 'pub_date']
        widgets = {
            'pub_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }