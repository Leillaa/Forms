from django.shortcuts import redirect, render, get_object_or_404

from .models import Answer
from questionnaire.models import Questionnaire
from questionnaire.forms import PointForm


def index(request):
    return render(request, 'survey/index.html')

def get_answer(request, questionnaire, point):
    form = PointForm(request.POST or None)
    if form.is_valid():
        for q in form.questions:
            answer = Answer(
                survey=questionnaire,
                question=q,
                name=answer
            )
            answer.save()
        return 
    return render(
            request,
            'survey/point.html',
            context={questionnaire: questionnaire, point: point}
        )

def create_new_survey(request, pk=None):
    questionnaire = get_object_or_404(Questionnaire, id=pk)
    for point in questionnaire.points.all():
        print(point)
        get_answer(request, questionnaire, point)
    return render(request, 'survey/success.html')

