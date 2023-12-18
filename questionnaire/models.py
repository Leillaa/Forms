from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
Q_TYPES = (
        ('text', 'text'),
        ('radio', 'radio'),
        ('check_box', 'check_box'),
        ('raiting', 'raiting'),
        ('text_or_non', 'text_or_non')
    )


class Questionnaire(models.Model):
    """Модель анкеты"""
    name = models.TextField('Название опроса')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='questionnaries'
    )
    published = models.BooleanField('Опубликовано', default=False)
    start_date = models.DateField('Начало анкетирования', auto_now=True)
    finish_date = models.DateField('Окончание анкетирования', blank=True, null=True)
    finished = models.BooleanField('Окончен', default=False)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        if self.finished:
            status = 'Завершен'
        elif self.published:
            status = 'Проводится'
        else:
            status = f'Начнется {self.start_date}'
        return f'{self.name}, статус: {status}'


class Point(models.Model):
    """Модель пункта анкеты"""
    name = models.CharField(
        'Пункт в анкете',
        max_length=250
    )
    number = models.PositiveIntegerField(
        'Номер в анкете'
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        related_name='points'
    )
    type_point = models.CharField(
        'Тип вопросов', 
        choices=Q_TYPES,
        max_length=12
    )
    num_column = models.SmallIntegerField('Кол-во колонок')

    class Meta:
        ordering = ['number']
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'

    def __str__(self) -> str:
        return str(self.name)

class Question(models.Model):
    """Модель вопроса в пункте"""
    name = models.CharField(
        'Вопрос',
        max_length=250
    )
    point = models.ForeignKey(
        Point,
        on_delete=models.CASCADE,
        verbose_name='Пункт в Анкете',
        related_name='questions'
    )
    number = models.PositiveIntegerField(
        'Номер в пункте'
    )

    class Meta:
        ordering = ['-number']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return str(self.name)


class Answer(models.Model):
    name = models.CharField(
        'Ответ',
        max_length=100
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='variants'
    )

