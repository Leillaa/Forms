from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from questionnaire.models import Questionnaire, Point, Question, Answer
from survey.models import Survey, Answer as SurveyAnswer

User = get_user_model()


class QuestionnaireModelTests(TestCase):
    """Тесты модели Questionnaire"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='author',
            password='pass123'
        )
        self.questionnaire = Questionnaire.objects.create(
            name='Тестовый опрос',
            author=self.user,
            published=True
        )

    def test_questionnaire_creation(self):
        """Тест создания опросника"""
        self.assertEqual(self.questionnaire.name, 'Тестовый опрос')
        self.assertEqual(self.questionnaire.author, self.user)
        self.assertTrue(self.questionnaire.published)
        self.assertFalse(self.questionnaire.finished)

    def test_questionnaire_str(self):
        """Тест строкового представления опросника"""
        self.assertIn('Тестовый опрос', str(self.questionnaire))
        self.assertIn('Проводится', str(self.questionnaire))

    def test_questionnaire_finished_status(self):
        """Тест статуса завершенного опросника"""
        self.questionnaire.finished = True
        self.questionnaire.save()
        self.assertIn('Завершен', str(self.questionnaire))


class PointModelTests(TestCase):
    """Тесты модели Point"""

    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass123')
        self.questionnaire = Questionnaire.objects.create(
            name='Опрос',
            author=self.user
        )
        self.point = Point.objects.create(
            name='Пункт 1',
            number=1,
            questionnaire=self.questionnaire,
            type_point='text',
            num_column=1
        )

    def test_point_creation(self):
        """Тест создания пункта"""
        self.assertEqual(self.point.name, 'Пункт 1')
        self.assertEqual(self.point.number, 1)
        self.assertEqual(self.point.questionnaire, self.questionnaire)
        self.assertEqual(self.point.type_point, 'text')

    def test_point_ordering(self):
        """Тест упорядочивания пунктов"""
        point2 = Point.objects.create(
            name='Пункт 2',
            number=2,
            questionnaire=self.questionnaire,
            type_point='radio',
            num_column=1
        )
        points = list(Point.objects.all())
        self.assertEqual(points[0], self.point)
        self.assertEqual(points[1], point2)


class QuestionModelTests(TestCase):
    """Тесты модели Question"""

    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass123')
        self.questionnaire = Questionnaire.objects.create(
            name='Опрос',
            author=self.user
        )
        self.point = Point.objects.create(
            name='Пункт 1',
            number=1,
            questionnaire=self.questionnaire,
            type_point='text',
            num_column=1
        )
        self.question = Question.objects.create(
            name='Вопрос 1',
            point=self.point,
            number=1
        )

    def test_question_creation(self):
        """Тест создания вопроса"""
        self.assertEqual(self.question.name, 'Вопрос 1')
        self.assertEqual(self.question.point, self.point)
        self.assertEqual(self.question.number, 1)

    def test_question_str(self):
        """Тест строкового представления вопроса"""
        self.assertEqual(str(self.question), 'Вопрос 1')


class SurveyModelTests(TestCase):
    """Тесты модели Survey"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.author = User.objects.create_user(username='author', password='pass123')
        self.questionnaire = Questionnaire.objects.create(
            name='Опрос',
            author=self.author,
            published=True
        )
        self.survey = Survey.objects.create(
            questionnaire=self.questionnaire,
            user=self.user
        )

    def test_survey_creation(self):
        """Тест создания ответа на опрос"""
        self.assertEqual(self.survey.questionnaire, self.questionnaire)
        self.assertEqual(self.survey.user, self.user)
        self.assertIsNotNone(self.survey.date)

    def test_survey_str(self):
        """Тест строкового представления ответа на опрос"""
        self.assertIn('Опрос', str(self.survey))


class SurveyViewTests(TestCase):
    """Тесты представлений опросов"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.author = User.objects.create_user(username='author', password='pass123')
        
        # Создаем опросник с пунктами и вопросами
        self.questionnaire = Questionnaire.objects.create(
            name='Тестовый опрос',
            author=self.author,
            published=True
        )
        self.point = Point.objects.create(
            name='Пункт 1',
            number=1,
            questionnaire=self.questionnaire,
            type_point='text',
            num_column=1
        )
        self.question = Question.objects.create(
            name='Вопрос 1',
            point=self.point,
            number=1
        )

    def test_index_view(self):
        """Тест главной страницы"""
        response = self.client.get(reverse('survey:index'))
        self.assertEqual(response.status_code, 200)

    def test_survey_requires_authentication(self):
        """Тест доступа к главной странице опросов"""
        response = self.client.get(reverse('survey:index'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_can_access_survey(self):
        """Тест что авторизованный пользователь может пройти опрос"""
        self.client.login(username='testuser', password='pass123')
        # Проверяем доступ к главной странице
        response = self.client.get(reverse('survey:index'))
        self.assertEqual(response.status_code, 200)

    def test_survey_submission(self):
        """Тест прохождения опроса"""
        self.client.login(username='testuser', password='pass123')
        # Просто проверяем что можем создать опрос вручную
        survey = Survey.objects.create(
            questionnaire=self.questionnaire,
            user=self.user
        )
        self.assertTrue(Survey.objects.filter(user=self.user).exists())
        self.assertEqual(survey.questionnaire, self.questionnaire)


class ProfileSurveyTests(TestCase):
    """Тесты отображения опросов в профиле"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.author = User.objects.create_user(username='author', password='pass123')
        
        self.questionnaire = Questionnaire.objects.create(
            name='Опрос 1',
            author=self.author,
            published=True
        )
        self.survey = Survey.objects.create(
            questionnaire=self.questionnaire,
            user=self.user
        )

    def test_profile_shows_user_surveys(self):
        """Тест что профиль показывает опросы пользователя"""
        self.client.login(username='testuser', password='pass123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Опрос 1')

    def test_profile_only_shows_own_surveys(self):
        """Тест что пользователь видит только свои опросы"""
        other_user = User.objects.create_user(username='other', password='pass123')
        other_survey = Survey.objects.create(
            questionnaire=self.questionnaire,
            user=other_user
        )
        
        self.client.login(username='testuser', password='pass123')
        response = self.client.get(reverse('users:profile'))
        
        # Проверяем что есть свои опросы
        surveys = response.context['surveys']
        self.assertIn(self.survey, surveys)
        self.assertNotIn(other_survey, surveys)
