from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from survey.models import Answer, Survey
from questionnaire.models import Question, Questionnaire, Point


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all___'

    def create(self, data):
        Survey.objects.create(
            questionnaire=data['questionnaire']
        )
        return Response(serializers)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
    
    def validate(self, data):
        survey = Survey.objects.get_or_create(questionnaire=data['questionnaire'])
        question = get_object_or_404(Question, id=data['question'])
        if not survey:
            raise serializers.ValidationError('Нет опроса')
    
    def create(self, validated_data):
        survey = Survey(questionnaire=validated_data.pop('question'))
        question = validated_data.pop('question')
        answer = Answer.objects.create(survey=survey, **validated_data)
        return answer



class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'
    

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PointSerializers(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'
    