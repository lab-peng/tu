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


# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = SampleModel
#         exclude = ['text', 'decimal', 'float_info']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['bool'] = forms.ChoiceField(choices=((True, 'Yes'), (False, 'No')), widget=forms.Select)
#         for k in self.fields.keys():
#             # if k != 'bool':
#             self.fields[k].widget.attrs.update({
#                 'class': 'form-control',
#             })


years = ['2020', '2021', '2022']
integers = [
    ('100', '100'),
    ('200', '200'),
    ('300', '300'),
]

class SearchForm(forms.Form):
    char__icontains = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date__in = forms.DateField(widget=forms.SelectDateWidget(years=years))
    integer__in = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=integers,
    )
