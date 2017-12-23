from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TrackForm
from .models import Training
import datetime


@login_required
def add(request):
    if request.method == 'POST':
        form = TrackForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            training = form.save()
            messages.success(request, 'Training successfuly imported!')
            return redirect('training:show', pk=training.pk)
        else:
            messages.warning(request, 'Incorrect training input!')
            return render(request, 'training.html', {'form': form})
    form = TrackForm(request.user)
    return render(request, 'training.html', {'form': form})


@login_required
def show(request, pk):
    training = Training.objects.get(pk=pk)
    return render(request, 'training_show.html', {'training': training})


@login_required
def show_all(request):
    trainings = Training.objects.filter(user=request.user)
    return render(request, 'training_list.html', {'trainings': trainings})
