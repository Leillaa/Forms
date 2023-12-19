from django.shortcuts import redirect, render, get_object_or_404, HttpResponse

from .models import Answer, Survey
from .forms import AnswerForm
from questionnaire.models import Questionnaire
from questionnaire.forms import PointFormSet


def index(request):
    return render(request, 'survey/index.html')

def get_answer(request, survey, questionnaire, point):
    form = AnswerForm(request.POST or None)
    print(f'NENENE',request, survey, point)
    a = input(form.data)
    if form.is_valid():
        for q in point.questions.all():
            answer = Answer(
                survey=survey,
                question=q,
                name=form.cleaned_data['name']
            )
            answer.save()
        return
    context={
        'questionnaire': questionnaire,
        'point': point,
        'form': form,
        'questions': point.questions.all()}
    return render(
                request,
                'survey/point.html',
                context=context
            )

def create_new_survey(request, pk=None):
    questionnaire = get_object_or_404(Questionnaire, id=pk)
    survey = Survey.objects.create(questionnaire=questionnaire)
    for point in questionnaire.points.all():
        form = AnswerForm(request.POST or None, instance=None)
        if form.is_valid():
            for q in point.questions.all():
                answer =Answer(
                    survey=survey,
                    question=q,
                    answer=form.cleaned_data['name']
                )
                answer.save()
            form = AnswerForm()

        else:
            context={
                'questionnaire': questionnaire,
                'point': point,
                'form': form,
                'questions': point.questions.all()}
            return render(
                request,
                'survey/point.html',
                context=context
            )
        
    return render(request, 'survey/success.html')

