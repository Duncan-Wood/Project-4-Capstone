from rest_framework import generics, viewsets
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneyTracker
from .serializers import UserSerializer, StepSerializer, UserStepSerializer, TimeTrackerSerializer, UserAddictionSerializer, MoneyTrackerSerializer
# from .serializers import UserViewSet

from django.contrib.auth.models import User

# Admin Views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
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

class MoneySavedList(generics.ListCreateAPIView):
    queryset = MoneyTracker.objects.all()
    serializer_class = MoneyTrackerSerializer

class MoneySavedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyTracker.objects.all()
    serializer_class = MoneyTrackerSerializer