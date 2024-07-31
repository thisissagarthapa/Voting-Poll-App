# In admin.py

from django.contrib import admin
from .models import Question, Option

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text', 'votes']
