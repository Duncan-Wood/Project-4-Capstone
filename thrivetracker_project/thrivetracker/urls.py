from django.urls import path

from .views import StepList, StepDetail, UserStepList, UserStepDetail, TimeTrackerList, TimeTrackerDetail, UserAddictionList, UserAddictionDetail, MoneySavedList, MoneySavedDetail

urlpatterns = [
    # Step URLs
    path('steps/', StepList.as_view(), name='step-list'),
    path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),

    # UserStep URLs
    path('usersteps/', UserStepList.as_view(), name='userstep-list'),
    path('usersteps/<int:pk>/', UserStepDetail.as_view(), name='userstep-detail'),

    # TimeTracker URLs
    path('timetrackers/', TimeTrackerList.as_view(), name='timetracker-list'),
    path('timetrackers/<int:pk>/', TimeTrackerDetail.as_view(), name='timetracker-detail'),

    # UserAddiction URLs
    path('useraddictions/', UserAddictionList.as_view(), name='useraddiction-list'),
    path('useraddictions/<int:pk>/', UserAddictionDetail.as_view(), name='useraddiction-detail'),

    # MoneySaved URLs
    path('moneysaved/', MoneySavedList.as_view(), name='moneysaved-list'),
    path('moneysaved/<int:pk>/', MoneySavedDetail.as_view(), name='moneysaved-detail'),
]