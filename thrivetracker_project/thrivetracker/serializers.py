from rest_framework import serializers
from .models import UserProfile, Step, UserStep, TimeTracker, UserAddiction, MoneyTracker

# Admin Serializers

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
    # come back and add functionality to add a money tracker to a time tracker, but not show the time tracker in the time tracker serializer (only show the money tracker)
    class Meta:
        model = MoneyTracker
        fields = ('id', 'amount')

class TimeTrackerSerializer(serializers.ModelSerializer):
    user_addiction = serializers.PrimaryKeyRelatedField(queryset=UserAddiction.objects.all())
    money_tracker = MoneyTrackerSerializer()

    class Meta:
        model = TimeTracker
        fields = ('id', 'user', 'user_addiction', 'start_time', 'end_time', 'duration', 'money_tracker')

class UserProfileSerializer(serializers.ModelSerializer):
    user_step = UserStepSerializer(many=True)
    user_addiction = UserAddictionSerializer(many=True)
    time_tracker = TimeTrackerSerializer(many=True)
    money_tracker = MoneyTrackerSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'user_step', 'user_addiction', 'time_tracker', 'money_tracker')