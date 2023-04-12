from rest_framework import serializers
from .models import *

class UserAddictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddiction
        fields = '__all__'

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

class TimeTrackerSerializer(serializers.ModelSerializer):
    user_addiction = UserAddictionSerializer()
    savings = SavingSerializer()

    class Meta:
        model = TimeTracker
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'



## Meant to work on After GA! IGNORE FOR NOW!!

# from .models import UserProfile, Step, UserStep

# class StepSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Step
#         fields = ('id', 'step', 'description')

# class UserStepSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserStep
#         fields = ['id', 'user', 'step', 'date', 'status', 'completed_at']

# class UserProfileSerializer(serializers.ModelSerializer):
#     user_addiction = UserAddictionSerializer(many=True)
#     time_tracker = TimeTrackerSerializer(many=True)
#     money_tracker = MoneyTrackerSerializer(many=True)

#     class Meta:
#         model = UserProfile
#         fields = ('id', 'user', 'user_addiction', 'time_tracker', 'money_tracker')