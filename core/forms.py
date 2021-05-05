from django import forms
from .models import AuthorInfo,ContentInfo,PaperAfter


class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorInfo
        fields = "__all__"


class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentInfo
        fields = "__all__"


class AfterForm(forms.ModelForm):
    class Meta:
        model = PaperAfter
        fields = '__all__'