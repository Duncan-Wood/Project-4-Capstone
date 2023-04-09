from rest_framework import serializers
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneyTracker
from django.contrib.auth.models import User

# Admin Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'name', 'description')

class UserStepSerializer(serializers.ModelSerializer):
    step = StepSerializer()
    user = UserSerializer()

    class Meta:
        model = UserStep
        fields = ('id', 'user', 'step', 'completed', 'completed_at')

class TimeTrackerSerializer(serializers.ModelSerializer):
    user_step = UserStepSerializer()

    class Meta:
        model = TimeTracker
        fields = ('id', 'user_step', 'time_spent', 'date')

class UserAddictionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    time_trackers = TimeTrackerSerializer(many=True, read_only=True)

    class Meta:
        model = UserAddiction
        fields = ('id', 'user', 'name', 'description', 'start_date', 'time_trackers')

class MoneyTrackerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MoneyTracker
        fields = ('id', 'user', 'duration', 'amount', 'time_tracker', 'currency')