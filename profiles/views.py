from django.shortcuts import render, redirect

from profiles.forms import ProfileForm
from profiles.models import Profile
from skills.models import Skill


def home_page(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ProfileForm()
        context = {
            'form': form,
        }

        return render(request, 'profiles/home-no-profile.html', context)
    context = {
        'profile': profile,
        'skills': skills,
    }
    return render(request, 'profiles/home.html', context)

def profile_details(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile-details.html', context)
