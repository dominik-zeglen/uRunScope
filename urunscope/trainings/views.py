from django.shortcuts import render, redirect
from .forms import TrackForm


def add(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track:add')
    form = TrackForm()
    return render(request, 'training.html', {'form': form})
