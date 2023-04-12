from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'tokens', TokenViewSet, basename='token')

urlpatterns = [
    # UserAddiction URLs
    path('addictions/', UserAddictionList.as_view(), name='user-addiction-list'),
    path('addictions/<int:pk>/', UserAddictionDetail.as_view(), name='user-addiction-detail'),

    # TimeTracker URLs
    path('time-trackers/', TimeTrackerList.as_view(), name='time-tracker-list'),
    path('time-trackers/<int:pk>/', TimeTrackerDetail.as_view(), name='time-tracker-detail'),

    # Note URLs
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),

    # Savings URLs
    path('savings/', SavingList.as_view(), name='savings-list'),
    path('savings/<int:pk>/', SavingDetail.as_view(), name='savings-detail'),


    
    ## Meant to work on After GA! IGNORE FOR NOW!!
    # # Step URLs
    # path('steps/', StepList.as_view(), name='step-list'),
    # path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),

    # # UserStep URLs
    # path('user-steps/', UserStepList.as_view(), name='user-step-list'),
    # path('user-steps/<int:pk>/', UserStepDetail.as_view(), name='user-step-detail'),
    # ## user URLs
    # path('users/', UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

urlpatterns += router.urls