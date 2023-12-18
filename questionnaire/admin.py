from django.contrib import admin

from .forms import ElementInLineFormSet
from .models import Questionnaire, Point, Question


class QuestionInLine(admin.TabularInline):
    model = Question
    formset = ElementInLineFormSet
    extra = 1


class PointInLine(admin.TabularInline):
    model = Point
    formset = ElementInLineFormSet
    extra = 1


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
    inlines = [QuestionInLine]


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'published', 'start_date', 'finish_date', 'finished']
    inlines = [PointInLine]
