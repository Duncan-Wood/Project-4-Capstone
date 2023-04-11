from django.urls import path

from .views import UserList, UserDetail, StepList, StepDetail, UserStepList, UserStepDetail, TimeTrackerList, TimeTrackerDetail, UserAddictionList, UserAddictionDetail, MoneyTrackerList, MoneyTrackerDetail


urlpatterns = [
    # Step URLs
    path('steps/', StepList.as_view(), name='step-list'),
    path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),

    # UserStep URLs
    path('user-steps/', UserStepList.as_view(), name='user-step-list'),
    path('user-steps/<int:pk>/', UserStepDetail.as_view(), name='user-step-detail'),

    # TimeTracker URLs
    path('time-trackers/', TimeTrackerList.as_view(), name='time-tracker-list'),
    path('time-trackers/<int:pk>/', TimeTrackerDetail.as_view(), name='time-tracker-detail'),

    # UserAddiction URLs
    path('user-addictions/', UserAddictionList.as_view(), name='user-addiction-list'),
    path('user-addictions/<int:pk>/', UserAddictionDetail.as_view(), name='user-addiction-detail'),

    # # MoneySaved URLs
    # come back and add functionality to add a money tracker to a time tracker, but not show the time tracker in the time tracker serializer (only show the money tracker)
    path('money-trackers/', MoneyTrackerList.as_view(), name='money-tracker-list'),
    path('money-trackers/<int:pk>/', MoneyTrackerDetail.as_view(), name='money-tracker-detail'),
    
    ## user URLs
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]


# Virtual AA

# steer away from the steps because recovery is not linear
# Get tokens, rewards for time tracker milestones
 # you're on day 1/30 towards the next token
 # gameify the process of recovery
 # perfect for people not comfortable going to meetings
# Get rewards for posting diary posts/ moods/ triggers/ progress