from django.urls import path


from .views import index, create_new_survey, get_answer, survey_step


app_name = 'survey'

urlpatterns = [
    path('', index, name='index'),
    path('answers/<int:pk>/', create_new_survey, name='answers'),
    path('get_answer/', get_answer, name='get_answer')
    ,path('survey4/<int:question_number>/', survey_step, name='survey_step')
    ,path('survey5/<int:question_number>/', survey_step, {'questionnaire_id': 6}, name='survey5_step')
]
