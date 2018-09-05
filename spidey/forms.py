from django import forms
from spidey.models import SpiderPic


class ImageForm(forms.ModelForm):
    class Meta:
        model = SpiderPic
        fields = ('pic', )
        widgets = {
            'pic': forms.FileInput(attrs={'class': 'file-input'}),
        }