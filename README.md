# 📋 Survey Form – Platform for Creating and Taking Surveys

![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![REST](https://img.shields.io/badge/REST-API-orange.svg)
![Tests](https://img.shields.io/badge/Tests-28%20passed-success.svg)

A modern web platform for creating, managing, and taking surveys with an intuitive interface and multilingual support.

---

## 🎯 Key Features

### 👤 User Management
- **AJAX Registration** – instant registration without page reload  
- **Modal Windows** – modern UI/UX for login and signup  
- **Role System** – user, moderator, admin  
- **User Profile** – view completed surveys and statistics  
- **Auto Login** – after successful registration  

---

### 📝 Survey System
- **Flexible Structure** – supports multiple question types  
- **Modal Survey Window** – surveys displayed in a stylish modal overlay  
- **Question Types:**
  - Text – text answers  
  - Radio – single choice  
  - Checkbox – multiple choice  
  - Rating – rating scale  
  - Text or None – optional text field  
- **Multi-step Completion** – step-by-step navigation through questions  
- **Progress Saving** – automatic answer saving  
- **Survey History** – all completed surveys stored in the user profile  

---

### 🎨 UI/UX
- **Modern Design** – clean, minimalist Figma-style interface  
- **Responsive Layout** – works seamlessly across all devices  
- **Modal Windows** – for registration, login, and surveys  
- **Overlay Effect** – background dimming when modals are open  
- **Click-to-Close** – easy closing of modals by clicking outside  
- **Animations & Transitions** – smooth UI interactions  

---

### 🌍 Multilingual Support
- **Google Translate Integration** – automatic translation of the entire site  
- **Custom Translate Button** – sleek mini-button in the site header  
- **One-Click Switching** – instant translation toggle  
- **Hidden Widget** – Google Translate runs quietly in the background  

---

### 🔐 Security
- **Django Authentication** – built-in secure auth system  
- **CSRF Protection** – against cross-site request forgery  
- **Data Validation** – strict input validation  
- **Password Hashing** – safe storage of credentials  

---

### 🧪 Testing
- **28 Automated Tests** – 100% coverage of core functionality  
- **Unit Tests** – for models, views, and forms  
- **Integration Tests** – for component interactions  
- **API Tests** – for AJAX and REST endpoints  

---

## 🛠 Technology Stack

### Backend
- **Django 5.2.7** – main framework  
- **Django REST Framework 3.16.1** – API endpoints  
- **SQLite** – database (easily switchable to PostgreSQL)  
- **Python 3.11** – programming language  

### Frontend
- **HTML5/CSS3** – structure and styling  
- **Vanilla JavaScript** – interactivity  
- **AJAX / Fetch API** – async requests  
- **Google Translate API** – multilingual interface  

### DevOps
- **Docker** – containerization  
- **Gunicorn** – production-ready WSGI server  
- **python-dotenv** – environment variable management  

---

## 📁 Project Structure

```
survey_form_2/
├── users/
│   ├── models.py
│   ├── views.py
│   ├── views_ajax.py
│   ├── forms.py
│   └── tests.py
├── survey/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── tests.py
├── questionnaire/
│   ├── models.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── create_standard_survey5.py
├── api/
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── survey/
│   │   ├── index.html
│   │   ├── point.html
│   │   └── success.html
│   └── users/
│       ├── signup.html
│       ├── profile.html
│       └── logged_out.html
├── static/
│   └── css/
│       └── style.css
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── manage.py
```

---

## 🚀 Installation & Setup

### Local Development

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SergSukh/survey_form_2.git
   cd survey_form_2
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venvs
   source venvs/bin/activate  # Linux/Mac
   venvs\Scripts\activate   # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **(Optional) Create Test Surveys**
   ```bash
   python manage.py create_standard_survey5
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

Visit the app at: `http://127.0.0.1:8000/`

---

### Docker Setup

1. **Build and Run Container**
   ```bash
   docker-compose up --build
   ```

2. **Run Migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Create Superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---

## 🧪 Running Tests

```bash
python manage.py test
python manage.py test --verbosity=2
python manage.py test users
python manage.py test survey
```

---

## 📊 Test Coverage
- ✅ **User Models** – creation, roles, permissions  
- ✅ **AJAX Registration** – success, validation errors, duplicates  
- ✅ **Authentication** – login, logout, password checks  
- ✅ **Profile** – access, survey display  
- ✅ **Survey Models** – creation, relations, ordering  
- ✅ **Survey Completion** – saving and filtering  
- ✅ **String Representations** – for all models  

---

## 🎨 Key Code Features

### AJAX Registration Without Page Reload
```javascript
document.getElementById('signupFormModal').addEventListener('submit', function(e) {
    e.preventDefault();
    fetch(ajaxUrl, {
        method: 'POST',
        body: new FormData(this),
        headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            showSuccessMessage();
            autoLogin();
        }
    });
});
```

### Modal Windows with Overlay
```css
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

### Dynamic Survey Forms
```python
def survey_step(request, question_number, questionnaire_id=4):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    points = questionnaire.points.all()
    if request.method == 'POST':
        survey = Survey.objects.create(
            questionnaire=questionnaire,
            user=request.user
        )
```

### Multilingual Support via Google Translate
```javascript
document.getElementById('translate-btn').addEventListener('click', function() {
    const select = document.querySelector('.goog-te-combo');
    if (select) {
        select.value = isEnglish ? 'ru' : 'en';
        select.dispatchEvent(new Event('change'));
        isEnglish = !isEnglish;
    }
});
```

---

## 📈 Project Metrics
- **Lines of Code:** ~2000  
- **Models:** 7  
- **Views:** 12+  
- **Tests:** 28 (100% passed)  
- **API Endpoints:** 5+  
- **Question Types:** 5  
- **Languages:** Unlimited  

---

## 🔄 API Endpoints

```
POST /users/ajax_signup/     # AJAX registration
POST /users/login/           # Login
POST /users/logout/          # Logout
GET  /users/profile/         # User profile

GET  /survey/                # Survey homepage
GET  /survey/survey4/<n>/    # Take survey #4
GET  /survey/survey5/<n>/    # Take survey #5
POST /survey/survey4/<n>/    # Submit answers

GET  /api/questionnaires/    # List all questionnaires
GET  /api/surveys/           # List completed surveys
```

---

## 🎓 What You’ll Learn
1. Django project structure & best practices  
2. AJAX integration for modern UX  
3. Modal windows without third-party libraries  
4. Writing unit and integration tests  
5. Building REST APIs with DRF  
6. Dynamic forms and data validation  
7. Django authentication system  
8. Docker containerization  
9. CSS Grid & Flexbox layouts  
10. Pure JavaScript interactivity  

---

## 🔮 Future Improvements
- [ ] Add analytics and visualizations for results  
- [ ] Export results to CSV/Excel  
- [ ] Shareable survey links  
- [ ] Notification system  
- [ ] Search and filtering  
- [ ] Comment system  
- [ ] Dark theme  
- [ ] OAuth integration (Google, Facebook)  

---

## 👨‍💻 Author
**Leila Chernova**  
- GitHub: [@Leillaa][https://github.com/Leillaa] 
- Project: [Forms](https://github.com/Leillaa/Forms/)

---

## 📄 License
This project was created for educational purposes and is available for use in both personal and commercial projects.

---

## 🙏 Acknowledgments
- Django Community for an excellent framework  
- Google Translate API for multilingual functionality  
- All open-source developers for their contributions  

---

⭐ If this project inspired or helped you, give it a star on GitHub! ⭐
