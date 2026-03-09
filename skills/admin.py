from django.contrib import admin

from skills.models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')