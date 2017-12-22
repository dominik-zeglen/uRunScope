from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TrackForm


def add(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('welcome'))
    form = TrackForm()
    return render(request, 'training.html', {'form': form})
