from bot_app.models import Answer, User,Test,Quection

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from bot_app.serializers import AnswerSerializer,UserSerializer,TestSerializer,QuectionSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
    def retrieve(self, request, *args, **kwargs):
        test = self.get_object()
        questions = test.questions.all()
        serializer = QuectionSerializer(questions,many=True)
        return Response(serializer.data)


class QuectionViewSet(ModelViewSet):
    queryset =Quection.objects.all()
    serializer_class = QuectionSerializer


class AnswerViewSet(ModelViewSet):
    queryset =Answer.objects.all()
    serializer_class = AnswerSerializer


class UserViewSet(ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer


