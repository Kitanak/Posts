from rest_framework import serializers

from bot_app.models import Test,Quection,Answer,User

from rest_framework.response import Response

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = (
            'id',
            'title',
            'user',
            )


class QuectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quection
        fields = (
            'id',
            'title',
            'test'
            )


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'id',
            'title',
            'quection',
            )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'telegram_id'
        )
    
    def create(self,validated_data):
        User = self.Meta.model 
        print(validated_data)
        print(validated_data.get("telegram_id"))
        user = User.objects.get_or_create(telegram_id=validated_data.get('telegram_id'))[0]
        return user
