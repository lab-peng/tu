from django import forms
from .models import SampleModel


class SampleModelForm(forms.ModelForm):
    class Meta:
        model = SampleModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bool'] = forms.ChoiceField(choices=((True, 'Yes'), (False, 'No')), widget=forms.RadioSelect)
        for k in self.fields.keys():
            if k != 'bool':
                self.fields[k].widget.attrs.update({
                    'class': 'form-control',
                })