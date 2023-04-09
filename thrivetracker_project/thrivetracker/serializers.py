from rest_framework import serializers
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneySaved

# Admin Seriazliers
class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'name', 'description', 'status', 'created_at', 'updated_at')

class UserStepSerializer(serializers.HyperlinkedModelSerializer):
    step = StepSerializer()
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        queryset=User.objects.all()
    )

    class Meta:
        model = UserStep
        fields = ('id', 'user', 'step', 'completed', 'completed_at')

class TimeTrackerSerializer(serializers.HyperlinkedModelSerializer):
    user_step = UserStepSerializer()

    class Meta:
        model = TimeTracker
        fields = ('id', 'user_step', 'time_spent', 'date')

class UserAddictionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        queryset=User.objects.all()
    )
    time_trackers = TimeTrackerSerializer(many=True, read_only=True)

    class Meta:
        model = UserAddiction
        fields = ('id', 'user', 'addiction', 'start_date', 'time_trackers')

class MoneySavedSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        queryset=User.objects.all()
    )

    class Meta:
        model = MoneySaved
        fields = ('id', 'user', 'amount_saved', 'currency')