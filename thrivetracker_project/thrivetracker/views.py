from .models import UserProfile, Step, UserStep, TimeTracker, UserAddiction, MoneyTracker
from .serializers import UserProfileSerializer, StepSerializer, UserStepSerializer, TimeTrackerSerializer, UserAddictionSerializer, MoneyTrackerSerializer
from rest_framework import generics

## Admin Views

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class StepList(generics.ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class StepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class UserStepList(generics.ListCreateAPIView):
    queryset = UserStep.objects.all()
    serializer_class = UserStepSerializer

class UserStepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserStep.objects.all()
    serializer_class = UserStepSerializer

class TimeTrackerList(generics.ListCreateAPIView):
    queryset = TimeTracker.objects.all()
    serializer_class = TimeTrackerSerializer

class TimeTrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeTracker.objects.all()
    serializer_class = TimeTrackerSerializer

class UserAddictionList(generics.ListCreateAPIView):
    queryset = UserAddiction.objects.all()
    serializer_class = UserAddictionSerializer

class UserAddictionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddiction.objects.all()
    serializer_class = UserAddictionSerializer

class MoneyTrackerList(generics.ListCreateAPIView):
    queryset = MoneyTracker.objects.all()
    serializer_class = MoneyTrackerSerializer

class MoneyTrackerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyTracker.objects.all()
    serializer_class = MoneyTrackerSerializer