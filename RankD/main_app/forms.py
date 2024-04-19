from django import forms
from .models import Platform

class PlatformForm(forms.Form):
    platform_choices = [(platform.id, platform.name) for platform in Platform.objects.all()]
    platform = forms.ChoiceField(choices=platform_choices, label='Select Platform')