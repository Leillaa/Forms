from django.urls import path

from .views import index, create_new_survey, get_answer


app_name = 'survey'

urlpatterns = [
    path('', index, name='index'),
    path('answers/<int:pk>/', create_new_survey, name='answers'),
    path('get_answer/', get_answer, name='get_answer')
]
