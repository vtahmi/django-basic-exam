from django.urls import path

from skills.views import skill_create, skill_details, SkillListView, skill_edit, skill_delete

urlpatterns = [
    path('', SkillListView.as_view(), name='skill-list'),
    path('create/', skill_create, name='skill-create'),
    path('<int:pk>/', skill_details, name='skill-details'),
    path('<int:pk>/edit/', skill_edit, name='skill-edit'),
    path('<int:pk>/delete/', skill_delete, name='skill-delete'),
]