from django.urls import path

from profiles.views import home_page, profile_details

urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', profile_details, name='profile-details'),
]
