from django.urls import path

from profiles.views import home_page, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', profile_details, name='profile-details'),
    path('edit/', profile_edit, name='profile-edit'),
    path('delete/', profile_delete, name='profile-delete'),
]
