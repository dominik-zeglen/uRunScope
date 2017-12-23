import os
import gpxpy
import datetime

from django import forms
from .models import Training
from django.core.exceptions import ValidationError


def point_to_dict(point):
    return {
        'lat': point.latitude,
        'lon': point.longitude,
        'elev': point.elevation,
        't': point.time.isoformat()
    }


def parse_gpx_data(gps_file):
    def iterate_points(data):
        for track in data.tracks:
            for segment in track.segments:
                for point in segment.points:
                    yield point
    gps_data = gpxpy.parse(gps_file)
    return [point_to_dict(p) for p in iterate_points(gps_data)]


class TrackForm(forms.ModelForm):
    track_file = forms.FileField(required=True, help_text='Upload gpx file')

    class Meta:
        model = Training
        fields = ['title']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_track_file(self):
        track = self.cleaned_data['track_file']
        ext = os.path.splitext(track.name)[1]
        if ext.lower() != '.gpx':
            raise ValidationError('File needs to be in gpx format!')
        track_file = track.read().decode("utf-8")
        self.track = parse_gpx_data(track_file)

    def save(self, commit=True):
        training = super().save(commit=False)
        training.track = self.track
        training.user = self.user
        # fake training processing for now
        training.distance = 1.00
        training.start_time = datetime.datetime.today()
        training.stop_time = datetime.datetime.today()
        training.duration = datetime.timedelta(0)
        if commit:
            training.save()
        return training
