from django.urls import path

from habits.views import habit_create, HabitListView, habit_edit, habit_delete

urlpatterns = [
    path('create/', habit_create, name='habit-create'),
    path('<int:pk>/edit/', habit_edit, name='habit-edit'),
    path('<int:pk>/delete/', habit_delete, name='habit-delete'),
    path('', HabitListView.as_view(), name='habit-list'),
]
