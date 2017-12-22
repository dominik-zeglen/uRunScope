from django import forms
from .models import Training


class TrackForm(forms.ModelForm):
    track_file = forms.FileField(
        required=True, help_text='Upload gpx file')

    class Meta:
        model = Training
        fields = ['title']
