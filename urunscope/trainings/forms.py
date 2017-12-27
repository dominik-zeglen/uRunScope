import os
import gpxpy
import decimal

from django import forms
from .models import Training
from django.core.exceptions import ValidationError
from training_stats import gpxfile
from io import StringIO

def point_to_dict(point):
    return {
        'lat': point.latitude,
        'lon': point.longitude,
        'elev': point.elevation,
        't': point.time
    }


def iterate_points(data):
    for track in data.tracks:
        for segment in track.segments:
            for point in segment.points:
                yield point


def parse_gpx_data(gps_file):
    gps_data = gpxpy.parse(gps_file)
    return [point_to_dict(p) for p in iterate_points(gps_data)]


def replace_time_with_delta(gps_track):
    begin = gps_track[0]['t']
    for point in gps_track:
        point['t'] = (point['t']-begin).total_seconds()


def get_times(gps_track):
    '''Requires sorted input ordered by time in ascending order'''
    start_time = gps_track[0]['t']
    stop_time = gps_track[-1]['t']
    duration = stop_time - start_time
    return start_time, stop_time, duration


def get_distance(gps_track):
    def coordinates(point):
        return (point['lat'], point['lon'])
    acc = 0.0
    last = coordinates(gps_track[0])
    for point in gps_track:
        new = coordinates(point)
        acc += gpxpy.geo.haversine_distance(*last, *new)
        last = new
    return decimal.Decimal(acc / 1000.0)


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
            raise ValidationError('File needs to be in gpx format')
        track_file = track.read().decode("utf-8")
        self.hrm = gpxfile.get_hr_measurements(StringIO(track_file))
        try:
            self.track = parse_gpx_data(track_file)
        except gpxpy.gpx.GPXException:
            raise ValidationError('File is not a valid gpx file')

    def save(self, commit=True):
        training = super().save(commit=False)
        start_t, stop_t, dt = get_times(self.track)
        replace_time_with_delta(self.track)
        training.track = self.track
        training.user = self.user
        training.start_time = start_t
        training.stop_time = stop_t
        training.duration = dt
        training.distance = get_distance(self.track)
        if self.hrm:
            training.hrm = self.hrm
        if commit:
            training.save()
        return training
