from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from habits.forms import HabitForm, HabitEditForm
from habits.models import Habit


def habit_create(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill-list')
    else:
        form = HabitForm()
    context = {
        'form': form
    }
    return render(request, 'habits/habit-create.html', context)

def habit_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    form = HabitEditForm(request.POST or None, instance=habit)
    if form.is_valid():
        form.save()
        return redirect('habit-list')
    context = {
        'form': form,
        'habit': habit
    }
    return render(request, 'habits/habit-edit.html', context)

def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect('habit-list')
    context = {
        'habit': habit
    }
    return render(request, 'habits/habit-delete.html', context)

class HabitListView(ListView):
    model = Habit
    template_name = 'habits/habit-list.html'
    context_object_name = 'habits'
    ordering = '-frequency'
