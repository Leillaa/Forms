from django.db import models
from django.contrib.auth import get_user_model

from questionnaire.models import Questionnaire, Question

User = get_user_model()


class Survey(models.Model):
    date = models.DateField('Дата опроса', auto_now_add=True)
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        related_name='surveys',
        verbose_name='Опрос'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='surveys',
        verbose_name='Пользователь',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Ответ на опрос'
        verbose_name_plural = 'Ответы на опросы'

    def __str__(self) -> str:
        return f'Ответы на вопросы {self.questionnaire}'


class Answer(models.Model):
    name = models.CharField(
        'Ответ',
        max_length=100,
    )
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='surveys'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
    )

    def get_question(self):
        return self.survey.questionnaire.points.question

