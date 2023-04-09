from rest_framework import serializers
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneyTracker
from django.contrib.auth.models import User

# Admin Serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'name', 'description')

class UserStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStep
        fields = ['id', 'user', 'step', 'date', 'status', 'completed_at']

class UserAddictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddiction
        fields = ('id', 'user', 'addiction', 'description')

class TimeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTracker
        fields = ('id', 'user', 'start_time', 'end_time', 'duration')

class MoneyTrackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoneyTracker
        fields = ('id', 'user', 'time_tracker', 'amount')
