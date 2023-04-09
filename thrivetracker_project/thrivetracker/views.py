from django.shortcuts import render

from rest_framework import generics
from .models import Step, UserStep, TimeTracker, UserAddiction, MoneySaved
from .serializers import StepSerializer, UserStepSerializer, TimeTrackerSerializer, UserAddictionSerializer, MoneySavedSerializer


# Create your views here.

# Admin Views

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
    queryset = MoneySaved.objects.all()
    serializer_class = MoneySavedSerializer

class MoneySavedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneySaved.objects.all()
    serializer_class = MoneySavedSerializer