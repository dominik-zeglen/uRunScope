from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


@login_required
def show(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': profile
    })


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, instance=profile)
        if form.is_valid():
            profile = form.save()
        else:
            messages.warning(request, 'Incorrect user data!')
            return render(request, 'profile_edit.html', {'form': form})

    form = ProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {'form': form})
