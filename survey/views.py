
from questionnaire.models import Point, Question, Answer as VariantAnswer

def survey_step(request, questionnaire_id=4, question_number=1):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    points = Point.objects.filter(questionnaire=questionnaire).order_by('number')
    total_questions = points.count()
    if question_number < 1 or question_number > total_questions:
        return render(request, 'survey/point.html', {
            'questionnaire': questionnaire,
            'success': True,
        })
    point = points[question_number-1]
    q_type = point.type_point
    variants = Question.objects.filter(point=point) if q_type in ['radio', 'check_box'] else []
    error = None
    if request.method == 'POST':
        answer_val = request.POST.getlist('answer') if q_type == 'check_box' else request.POST.get('answer')
        if q_type == 'text' and not answer_val:
            error = 'Заполните поле'
        elif q_type == 'raiting' and (not answer_val or not str(answer_val).isdigit() or not (1 <= int(answer_val) <= 5)):
            error = 'Выберите оценку от 1 до 5'
        elif q_type == 'radio' and not answer_val:
            error = 'Выберите вариант'
        if not error:
            survey = Survey.objects.filter(questionnaire=questionnaire, user=request.user).order_by('-id').first()
            if not survey:
                survey = Survey.objects.create(questionnaire=questionnaire, user=request.user)
            if q_type == 'check_box':
                for val in answer_val:
                    variant = Question.objects.filter(id=val, point=point).first()
                    if variant:
                        Answer.objects.create(name=variant.name, question=variant, survey=survey)
            elif q_type == 'radio':
                if answer_val:
                    variant = Question.objects.filter(id=answer_val, point=point).first()
                    if variant:
                        Answer.objects.create(name=variant.name, question=variant, survey=survey)
            else:
                if answer_val:
                    variant = Question.objects.filter(point=point).first()
                    if variant:
                        Answer.objects.create(name=answer_val, question=variant, survey=survey)
            # Если последний вопрос, показываем успех
            if question_number+1 > total_questions:
                return render(request, 'survey/point.html', {
                    'questionnaire': questionnaire,
                    'success': True,
                })
            # Переход по правильному маршруту
            if questionnaire_id == 4:
                return redirect('survey:survey_step', question_number=question_number+1)
            elif questionnaire_id == 6:
                return redirect('survey:survey5_step', question_number=question_number+1)
    return render(request, 'survey/point.html', {
        'questionnaire': questionnaire,
        'point': point,
        'q_type': q_type,
        'variants': variants,
        'question_number': question_number,
        'error': error,
        'total_questions': total_questions,
    })
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse

from .models import Answer, Survey
from .forms import AnswerForm
from questionnaire.models import Questionnaire
from questionnaire.forms import PointFormSet


def index(request):
    from users.forms import CreationForm
    form = CreationForm()
    return render(request, 'survey/index.html', {'form': form})

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

