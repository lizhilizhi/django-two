from django import forms
from . import models

class Api(forms.ModelForm):
    def clean_methon(self):
        methon =self.changed_data.get('methon')
        if len(methon) >3:
            raise forms.ValidationError('方法不对')
        return methon

    class Meta:
        model  = models.Question
        fields = '__all__'