from django.urls import path

from .views import index


app_name = 'survey'

urlpatterns = [
    path('', index, name='index')
]