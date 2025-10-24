from django.contrib.auth import get_user_model
from rest_framework import viewsets

from survey.models import Survey, Answer
from questionnaire.models import Question, Questionnaire, Point
from .serializers import SurveySerializer, AnswerSerializer, PointSerializers


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializers
