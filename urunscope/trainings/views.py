from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TrackForm


@login_required
def add(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            training.save()
            messages.success(request, 'Training successfuly imported!')
            return redirect('training:show', pk=training.pk)
        else:
            messages.warning(request, 'Incorrect training input!')
            return render(request, 'training.html', {'form': form})
    form = TrackForm()
    return render(request, 'training.html', {'form': form})
