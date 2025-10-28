# 📋 Survey Form - Платформа для создания и прохождения опросов

![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![REST](https://img.shields.io/badge/REST-API-orange.svg)
![Tests](https://img.shields.io/badge/Tests-28%20passed-success.svg)

Современная веб-платформа для создания, управления и прохождения опросов с интуитивным интерфейсом и мультиязычной поддержкой.

## 🎯 Основные возможности

### 👤 Управление пользователями
- **Регистрация через AJAX** - мгновенная регистрация без перезагрузки страницы
- **Модальные окна** - современный UI/UX для входа и регистрации
- **Система ролей** - user, moderator, admin
- **Профиль пользователя** - просмотр пройденных опросов и статистики
- **Автоматический вход** - после успешной регистрации

### 📝 Система опросов
- **Гибкая структура** - поддержка множественных типов вопросов
- **Модальное окно опроса** - опросы отображаются в стильном модальном окне поверх страницы
- **Типы вопросов**:
  - Text - текстовые ответы
  - Radio - выбор одного варианта
  - Checkbox - множественный выбор
  - Rating - рейтинговая шкала
  - Text or None - опциональный текст
- **Многоэтапное прохождение** - пошаговая навигация по вопросам
- **Сохранение прогресса** - автоматическое сохранение ответов
- **История опросов** - все пройденные опросы сохраняются в профиле

### 🎨 UI/UX
- **Современный дизайн** - чистый минималистичный интерфейс в стиле Figma
- **Адаптивная верстка** - работает на всех устройствах
- **Модальные окна** - для регистрации, входа и прохождения опросов
- **Overlay эффект** - затемнение фона при открытии модальных окон
- **Закрытие по клику** - удобное закрытие модальных окон кликом вне области
- **Анимации и переходы** - плавные transition эффекты

### 🌍 Мультиязычность
- **Google Translate интеграция** - автоматический перевод всего сайта
- **Кастомная кнопка перевода** - стильная мини-кнопка в шапке сайта
- **Переключение языков** - мгновенный перевод одним кликом
- **Скрытый виджет** - Google Translate работает в фоне без визуального мусора

### 🔐 Безопасность
- **Аутентификация Django** - встроенная система безопасности
- **CSRF защита** - защита от межсайтовой подделки запросов
- **Валидация данных** - проверка всех пользовательских данных
- **Хеширование паролей** - безопасное хранение паролей

### 🧪 Тестирование
- **28 автоматических тестов** - 100% coverage критической функциональности
- **Unit тесты** - тестирование моделей, представлений и форм
- **Integration тесты** - тестирование взаимодействия компонентов
- **Тесты API** - проверка AJAX endpoints

## 🛠 Технологический стек

### Backend
- **Django 5.2.7** - основной фреймворк
- **Django REST Framework 3.16.1** - API endpoints
- **SQLite** - база данных (легко мигрируется на PostgreSQL)
- **Python 3.11** - язык программирования

### Frontend
- **HTML5/CSS3** - разметка и стили
- **JavaScript (Vanilla)** - интерактивность
- **AJAX/Fetch API** - асинхронные запросы
- **Google Translate API** - мультиязычность

### DevOps
- **Docker** - контейнеризация приложения
- **Gunicorn** - production WSGI сервер
- **python-dotenv** - управление переменными окружения

## 📁 Структура проекта

```
survey_form_2/
├── users/              # Приложение управления пользователями
│   ├── models.py       # Модель User с ролями
│   ├── views.py        # Представления регистрации, профиля
│   ├── views_ajax.py   # AJAX endpoints
│   ├── forms.py        # Формы регистрации
│   └── tests.py        # Тесты пользователей (13 тестов)
├── survey/             # Приложение опросов
│   ├── models.py       # Модели Survey, Answer
│   ├── views.py        # Представления прохождения опросов
│   ├── forms.py        # Динамические формы опросов
│   └── tests.py        # Тесты опросов (15 тестов)
├── questionnaire/      # Приложение управления анкетами
│   ├── models.py       # Модели Questionnaire, Point, Question
│   ├── admin.py        # Административная панель
│   └── management/     # Команды управления
│       └── commands/
│           └── create_standard_survey5.py  # Создание тестовых опросов
├── api/                # REST API endpoints
│   ├── views.py        # API представления
│   ├── serializers.py  # Сериализаторы данных
│   └── urls.py         # API маршруты
├── templates/          # HTML шаблоны
│   ├── base.html       # Базовый шаблон
│   ├── survey/         # Шаблоны опросов
│   │   ├── index.html
│   │   ├── point.html  # Модальное окно опроса
│   │   └── success.html
│   └── users/          # Шаблоны пользователей
│       ├── signup.html
│       ├── profile.html
│       └── logged_out.html
├── static/             # Статические файлы
│   └── css/
│       └── style.css   # Стили сайта
├── Dockerfile          # Docker конфигурация
├── docker-compose.yaml # Docker Compose
├── requirements.txt    # Python зависимости
└── manage.py           # Django management команды
```

## 🚀 Установка и запуск

### Локальная разработка

1. **Клонирование репозитория**
```bash
git clone https://github.com/SergSukh/survey_form_2.git
cd survey_form_2
```

2. **Создание виртуального окружения**
```bash
python3 -m venv venvs
source venvs/bin/activate  # Linux/Mac
# или
venvs\Scripts\activate  # Windows
```

3. **Установка зависимостей**
```bash
pip install -r requirements.txt
```

4. **Применение миграций**
```bash
python manage.py migrate
```

5. **Создание суперпользователя**
```bash
python manage.py createsuperuser
```

6. **Создание тестовых опросов** (опционально)
```bash
python manage.py create_standard_survey5
```

7. **Запуск сервера разработки**
```bash
python manage.py runserver
```

Сайт будет доступен по адресу: `http://127.0.0.1:8000/`

### Docker

1. **Сборка и запуск контейнера**
```bash
docker-compose up --build
```

2. **Применение миграций в контейнере**
```bash
docker-compose exec web python manage.py migrate
```

3. **Создание суперпользователя в контейнере**
```bash
docker-compose exec web python manage.py createsuperuser
```

## 🧪 Запуск тестов

```bash
# Запуск всех тестов
python manage.py test

# Запуск тестов с подробным выводом
python manage.py test --verbosity=2

# Запуск тестов конкретного приложения
python manage.py test users
python manage.py test survey
```

## 📊 Покрытие тестами

- ✅ **Модели пользователей** - создание, роли, права доступа
- ✅ **Регистрация AJAX** - успех, ошибки валидации, дубликаты
- ✅ **Аутентификация** - вход, выход, проверка паролей
- ✅ **Профиль** - доступ, отображение опросов
- ✅ **Модели опросов** - создание, связи, упорядочивание
- ✅ **Прохождение опросов** - доступ, сохранение, фильтрация
- ✅ **Строковые представления** - `__str__` методы всех моделей

## 🎨 Ключевые функции кода

### AJAX регистрация без перезагрузки
```javascript
// users/templates/users/signup.html
document.getElementById('signupFormModal').addEventListener('submit', function(e) {
    e.preventDefault();
    fetch(ajaxUrl, {
        method: 'POST',
        body: new FormData(this),
        headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccessMessage();
            autoLogin();
        }
    });
});
```

### Модальные окна с overlay
```css
/* static/css/style.css */
.modal-survey {
    background: white;
    border-radius: 16px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    max-width: 600px;
    padding: 40px;
}

.modal-overlay {
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(4px);
}
```

### Динамические формы опросов
```python
# survey/views.py
def survey_step(request, question_number, questionnaire_id=4):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    points = questionnaire.points.all()
    
    if request.method == 'POST':
        # Сохранение ответов
        survey = Survey.objects.create(
            questionnaire=questionnaire,
            user=request.user
        )
        # Обработка и сохранение каждого ответа
```

### Мультиязычность с Google Translate
```javascript
// templates/base.html
document.getElementById('translate-btn').addEventListener('click', function() {
    var select = document.querySelector('.goog-te-combo');
    if (select) {
        select.value = isEnglish ? 'ru' : 'en';
        select.dispatchEvent(new Event('change'));
        isEnglish = !isEnglish;
    }
});
```

## 📈 Метрики проекта

- **Строк кода**: ~2000+
- **Моделей**: 7 (User, Questionnaire, Point, Question, Answer, Survey, SurveyAnswer)
- **Представлений**: 12+
- **Тестов**: 28 (100% passed)
- **API endpoints**: 5+
- **Типов вопросов**: 5
- **Языков интерфейса**: неограниченно (Google Translate)

## 🔄 API Endpoints

```
POST /users/ajax_signup/     # AJAX регистрация
POST /users/login/           # Вход в систему
POST /users/logout/          # Выход из системы
GET  /users/profile/         # Профиль пользователя

GET  /survey/                # Главная страница опросов
GET  /survey/survey4/<n>/    # Прохождение опроса #4
GET  /survey/survey5/<n>/    # Прохождение опроса #5
POST /survey/survey4/<n>/    # Сохранение ответов

GET  /api/questionnaires/    # Список опросников (REST API)
GET  /api/surveys/           # Список пройденных опросов
```

## 🎓 Чему можно научиться из этого проекта

1. **Django Best Practices** - структура проекта, модели, представления
2. **AJAX интеграция** - современный асинхронный UI
3. **Модальные окна** - создание без Bootstrap/сторонних библиотек
4. **Django тестирование** - unit и integration тесты
5. **REST API** - Django REST Framework
6. **Работа с формами** - динамические формы, валидация
7. **Аутентификация** - Django auth система
8. **Docker** - контейнеризация приложения
9. **CSS Grid/Flexbox** - современная верстка
10. **Vanilla JavaScript** - без jQuery и фреймворков

## 🔮 Возможные улучшения

- [ ] Добавить аналитику и визуализацию результатов опросов
- [ ] Реализовать экспорт результатов в CSV/Excel
- [ ] Добавить возможность делиться опросами по ссылке
- [ ] Интегрировать систему уведомлений
- [ ] Добавить поиск и фильтрацию опросов
- [ ] Реализовать систему комментариев
- [ ] Добавить темную тему
- [ ] Интегрировать OAuth (Google, Facebook)

## 👨‍💻 Автор

**Leila Chernova**
- GitHub: [@Leillaa](https://github.com/Leillaa)
- Проект: [Forms](https://github.com/Leillaa/Forms)

## 📄 Лицензия

Этот проект создан в образовательных целях и доступен для использования в личных и коммерческих проектах.

## 🙏 Благодарности

- Django Community за отличный фреймворк
- Google Translate API за мультиязычность
- Все разработчики open-source библиотек

---

⭐ Если этот проект помог вам, поставьте звезду на GitHub!
