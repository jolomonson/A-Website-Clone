from django.contrib import admin
from . models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Tutorial Title and Date", {"fields":["title","published"]}),
        ("Tutorial Content", {"fields":["content"]})
    )
    formfield_overrides = {
        models.TextField :{'widget':TinyMCE()}
    }
    
admin.site.register(Tutorial, TutorialAdmin)