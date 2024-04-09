from django import forms
from main_app.models import *

class LoginForm(forms.Form):
    email =  forms.CharField()
    password = forms.CharField()
    
class AddReviewForm(forms.ModelForm):
    platform = forms.ModelChoiceField(queryset=Platform.objects.all())
    comment = forms.CharField(max_length=1000)
    rating = forms.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )