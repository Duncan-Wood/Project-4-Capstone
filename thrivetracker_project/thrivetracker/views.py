from .models import *
from .serializers import *
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


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

class NoteListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    @action(detail=False, methods=['get'])
    def earned_tokens(self, request):
        user = self.request.user
        tokens = Token.objects.filter(user=user)
        serializer = self.get_serializer(tokens, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def token_detail(self, request, pk=None):
        token = self.get_object()
        serializer = self.get_serializer(token)
        return Response(serializer.data)
    


## Meant to work on After GA! IGNORE FOR NOW!!

# class UserList(generics.ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
    
# class StepList(generics.ListCreateAPIView):
#     queryset = Step.objects.all()
#     serializer_class = StepSerializer

# class StepDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Step.objects.all()
#     serializer_class = StepSerializer

# class UserStepList(generics.ListCreateAPIView):
#     queryset = UserStep.objects.all()
#     serializer_class = UserStepSerializer

# class UserStepDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserStep.objects.all()
#     serializer_class = UserStepSerializer