from django.core.management.base import BaseCommand
from questionnaire.models import Questionnaire, Point, Question
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Создаёт стандартный опрос №5 на 10 вопросов с разными типами.'

    def handle(self, *args, **options):
        User = get_user_model()
        admin = User.objects.filter(is_superuser=True).first()
        if not admin:
            self.stdout.write(self.style.ERROR('Нет суперпользователя!'))
            return
        qn = Questionnaire.objects.create(
            name='Стандартный опрос (10 вопросов)',
            author=admin,
            published=True
        )
        types = ['text', 'radio', 'check_box', 'raiting', 'text_or_non']
        for i in range(10):
            t = types[i % len(types)]
            point = Point.objects.create(
                name=f'Вопрос {i+1} ({t})',
                number=i+1,
                questionnaire=qn,
                type_point=t,
                num_column=1
            )
            if t in ['radio', 'check_box']:
                for j in range(1, 5):
                    Question.objects.create(
                        name=f'Вариант {j} для вопроса {i+1}',
                        point=point,
                        number=j
                    )
            else:
                # Для text/text_or_non/raiting — создаём фиктивный Question для связи
                Question.objects.create(
                    name=f'Ответ для вопроса {i+1}',
                    point=point,
                    number=1
                )
        self.stdout.write(self.style.SUCCESS('Опрос №5 создан!'))
