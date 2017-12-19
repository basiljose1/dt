from django import forms
from django.forms import ModelForm, ModelChoiceField

from app.models import LenderDetails, StateDetails, Lender 


class LenderForm(ModelForm):

    lender = ModelChoiceField(queryset=LenderDetails.objects, empty_label='Select a Lender')
    lender_state = ModelChoiceField(queryset=StateDetails.objects, empty_label='Select a State')

    class Meta:
        model = Lender
        fields = '__all__'
