from polls.models import Question
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

@api_view(['GET'])
def question_list(request):
    question_list = Question.objects.all()
    serializers = QuestionSerializer(question_list,many=True)
    return Response(serializers.data)
