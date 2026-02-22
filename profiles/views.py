from django.shortcuts import render, redirect

from habits.models import Habit
from profiles.forms import ProfileDetailsForm, ProfileForm
from profiles.models import Profile
from skills.models import Skill


def home_page(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    habits = Habit.objects.all()
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
        'habits': habits,
    }
    return render(request, 'profiles/home.html', context)

def profile_details(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    habits = Habit.objects.all()
    context = {
        'profile': profile,
        'skills': skills,
        'habits': habits,
    }
    return render(request, 'profiles/profile-details.html', context)

def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/profile-edit.html', context)

def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)

