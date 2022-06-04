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


dates = (
    ('2020-01-01', '2020-01-01'),
    ('2020-01-02', '2020-01-02'),
    ('2020-01-03', '2020-01-03'),
)

class SearchForm(forms.Form):
    char__icontains = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date__in = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=dates,
    )
