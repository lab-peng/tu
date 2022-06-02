from django import forms

from app_a.models import Project


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control'}