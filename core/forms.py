from django import forms
from .models import AuthorInfo,PaperAfter,AbstractInfo


class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorInfo
        fields = "__all__"

class AfterForm(forms.ModelForm):
    class Meta:
        model = PaperAfter
        fields = '__all__'

class AbstractForm(forms.ModelForm):
    class Meta:
        model = AbstractInfo
        fields = "__all__"