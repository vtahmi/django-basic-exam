from django.contrib import admin
from django.urls import path, include

from skills.views import SkillListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('profiles.urls')),
    path('skills/', include('skills.urls')),
    path('habits/', include('habits.urls')),
]
