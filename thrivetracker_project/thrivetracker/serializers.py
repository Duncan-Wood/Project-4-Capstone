from rest_framework import serializers
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneyTracker
from django.contrib.auth.models import User

## Admin Serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'step', 'description')

class UserStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStep
        fields = ['id', 'user', 'step', 'date', 'status', 'completed_at']

class UserAddictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddiction
        fields = ('id', 'user', 'addiction', 'description')

class MoneyTrackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoneyTracker
        fields = ('id', 'amount')

class TimeTrackerSerializer(serializers.ModelSerializer):
    user_addiction = serializers.PrimaryKeyRelatedField(queryset=UserAddiction.objects.all())
    money_tracker = MoneyTrackerSerializer()

    class Meta:
        model = TimeTracker
        fields = ('id', 'user', 'user_addiction', 'start_time', 'end_time', 'duration', 'money_tracker')