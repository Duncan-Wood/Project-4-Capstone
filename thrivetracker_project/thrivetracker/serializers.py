from rest_framework import serializers, viewsets
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneySaved
from django.contrib.auth.models import User

# Admin Seriazliers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

# This class is used to create a new user from the admin panel in the browser (not used in the API)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at')

class UserStepSerializer(serializers.HyperlinkedModelSerializer):
    step = StepSerializer()
    user = UserSerializer()

    class Meta:
        model = UserStep
        fields = ('id', 'user', 'step', 'completed', 'completed_at')

class TimeTrackerSerializer(serializers.HyperlinkedModelSerializer):
    user_step = UserStepSerializer()

    class Meta:
        model = TimeTracker
        fields = ('id', 'user_step', 'time_spent', 'date')

class UserAddictionSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    time_trackers = TimeTrackerSerializer(many=True, read_only=True)

    class Meta:
        model = UserAddiction
        fields = ('id', 'user', 'addiction', 'start_date', 'time_trackers')

class MoneySavedSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MoneySaved
        fields = ('id', 'user', 'amount_saved', 'currency')