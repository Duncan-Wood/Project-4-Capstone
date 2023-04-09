from django.urls import path, include

# from rest_framework.routers import DefaultRouter

from .views import StepList, StepDetail, UserStepList, UserStepDetail, TimeTrackerList, TimeTrackerDetail, UserAddictionList, UserAddictionDetail, MoneyTrackerList, MoneyTrackerDetail
# from .views import UserViewSet

# Create a router and register UserViewSet
# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # # Router URLs
    # path('', include(router.urls)),

    # Step URLs
    path('steps/', StepList.as_view(), name='step-list'),
    path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),

    # UserStep URLs
    path('user-steps/', UserStepList.as_view(), name='user-step-list'),
    path('usersteps/<int:pk>/', UserStepDetail.as_view(), name='user-step-detail'),

    # TimeTracker URLs
    path('time-trackers/', TimeTrackerList.as_view(), name='time-tracker-list'),
    path('time-trackers/<int:pk>/', TimeTrackerDetail.as_view(), name='time-tracker-detail'),

    # UserAddiction URLs
    path('user-addictions/', UserAddictionList.as_view(), name='user-addiction-list'),
    path('user-addictions/<int:pk>/', UserAddictionDetail.as_view(), name='user-addiction-detail'),

    # MoneySaved URLs
    path('money-trackers/', MoneyTrackerList.as_view(), name='money-tracker-list'),
    path('money-trackers/<int:pk>/', MoneyTrackerDetail.as_view(), name='money-tracker-detail'),
]