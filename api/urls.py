from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AnswerViewSet, PointViewSet


app_name = 'api'

router = DefaultRouter
router.register('answer', AnswerViewSet, basename='answers')
router.register('point', PointViewSet, basename='pointers')


urlpatterns = [
    path('', include(router.urls))
]

