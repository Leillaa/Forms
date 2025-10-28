from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTests(TestCase):
    """Тесты модели User"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )

    def test_user_creation(self):
        """Тест создания пользователя"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.role, 'user')

    def test_user_str(self):
        """Тест строкового представления пользователя"""
        self.assertEqual(str(self.user), 'testuser')

    def test_is_user_property(self):
        """Тест свойства is_user"""
        self.assertTrue(self.user.is_user)
        self.assertFalse(self.user.is_admin)

    def test_is_admin_property(self):
        """Тест свойства is_admin"""
        admin = User.objects.create_user(
            username='admin',
            password='admin123',
            role='admin'
        )
        self.assertTrue(admin.is_admin)
        self.assertFalse(admin.is_user)

    def test_superuser_is_admin(self):
        """Тест что суперпользователь считается админом"""
        superuser = User.objects.create_superuser(
            username='superuser',
            password='super123'
        )
        self.assertTrue(superuser.is_admin)


class UserRegistrationTests(TestCase):
    """Тесты регистрации пользователей"""

    def setUp(self):
        self.client = Client()

    def test_signup_ajax_success(self):
        """Тест успешной регистрации через AJAX"""
        response = self.client.post(
            reverse('users:ajax_signup'),
            data={
                'username': 'newuser',
                'password1': 'TestPass123!',
                'password2': 'TestPass123!',
                'first_name': 'New',
                'last_name': 'User'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertIn('Аккаунт создан', response_data['message'])
        # Проверяем что пользователь создан
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_ajax_password_mismatch(self):
        """Тест регистрации с несовпадающими паролями"""
        response = self.client.post(
            reverse('users:ajax_signup'),
            data={
                'username': 'newuser',
                'password1': 'TestPass123!',
                'password2': 'DifferentPass123!',
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data['success'])
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_signup_ajax_existing_username(self):
        """Тест регистрации с существующим именем пользователя"""
        User.objects.create_user(username='existing', password='pass123')
        response = self.client.post(
            reverse('users:ajax_signup'),
            data={
                'username': 'existing',
                'password1': 'TestPass123!',
                'password2': 'TestPass123!',
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data['success'])


class UserAuthenticationTests(TestCase):
    """Тесты аутентификации пользователей"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_success(self):
        """Тест успешного входа"""
        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'testuser',
                'password': 'testpass123'
            }
        )
        self.assertEqual(response.status_code, 302)  # Редирект после входа
        # Проверяем что пользователь залогинен
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)

    def test_login_wrong_password(self):
        """Тест входа с неправильным паролем"""
        # Просто проверяем что логин с неправильным паролем не работает
        logged_in = self.client.login(username='testuser', password='wrongpass')
        self.assertFalse(logged_in)

    def test_logout(self):
        """Тест выхода из системы"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


class UserProfileTests(TestCase):
    """Тесты профиля пользователя"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_profile_requires_authentication(self):
        """Тест что профиль требует аутентификации"""
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)  # Редирект на логин

    def test_profile_authenticated_user(self):
        """Тест доступа к профилю авторизованного пользователя"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
