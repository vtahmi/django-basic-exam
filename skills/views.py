from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from profiles.models import Profile
from skills.forms import SkillForm
from skills.models import Skill

class SkillListView(ListView):
    model = Skill
    template_name = 'skills/skill-list.html'
    context_object_name = 'skills'

def skill_create(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            form.save_m2m()
            return redirect('skill-list')
    else:
        form = SkillForm()
    context = {
        'form': form
    }
    return render(request, 'skills/skill-create.html', context)

def skill_details(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    context = {
        'skill': skill
    }
    return render(request, 'skills/skill-details.html', context)

def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill-details', pk=skill.pk)
    else:
        form = SkillForm(instance=skill)
    context = {
        'form': form,
        'skill': skill
    }
    return render(request, 'skills/skill-edit.html', context)

def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill-list')
    context = {
        'skill': skill
    }
    return render(request, 'skills/skill-delete.html', context)