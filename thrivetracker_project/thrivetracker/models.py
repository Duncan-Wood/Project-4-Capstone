from django.db import models
from django.conf import settings

from django.db import models
from django.conf import settings

class TimeTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_trackers', null=True)
    user_addiction = models.OneToOneField('UserAddiction', null=True, blank=True, on_delete=models.SET_NULL)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    savings = models.OneToOneField('Saving', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'TimeTracker for {self.user_addiction}'

class UserAddiction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_addictions', null=True)
    addiction = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.addiction}'

class Saving(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='savings', null=True)
    time_tracker = models.OneToOneField(TimeTracker, null=True, blank=True, on_delete=models.SET_NULL)
    money_per_day = models.DecimalField(max_digits=100, decimal_places=2)
    time_per_day = models.DurationField()

    def __str__(self):
        return f'Savings for {self.user}'

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=150)
    mood = models.CharField(max_length=150)
    triggers = models.TextField()
    body = models.TextField()
    time_tracker = models.ForeignKey(TimeTracker, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)

    def __str__(self):
        return self.title

class Token(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tokens')
    name = models.CharField(max_length=150)
    description = models.TextField()
    earned_at = models.DateTimeField(auto_now_add=True)
    time_tracker = models.ForeignKey(TimeTracker, on_delete=models.CASCADE, related_name='tokens', null=True, blank=True)

    def __str__(self):
        return self.name
    

    
## Meant to work on After GA! IGNORE FOR NOW!!

# import datetime
# from django.contrib.auth.models import User

# class Step(models.Model):
#     step = models.CharField(max_length=150)
#     description = models.TextField()

#     def __str__(self):
#         return self.step

# class UserStep(models.Model):
#     USER_STEP_STATUS_CHOICES = (
#         (0, 'Incomplete'),
#         (1, 'Complete'),
#     )
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_steps', null=True)
#     step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='step_usersteps', null=True)
#     date = models.DateField(default=datetime.date.today)
#     status = models.IntegerField(choices=USER_STEP_STATUS_CHOICES, default=0)
#     completed_at = models.DateTimeField(null=True, blank=True)  # Add completed_at field

#     def __str__(self):
#         return self.step.step
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # user_step = models.ForeignKey(UserStep, null=True, blank=True, on_delete=models.SET_NULL)
#     user_addiction = models.ForeignKey(UserAddiction, null=True, blank=True, on_delete=models.SET_NULL)
#     time_tracker = models.ForeignKey(TimeTracker, null=True, blank=True, on_delete=models.SET_NULL)
#     money_tracker = models.ForeignKey(MoneyTracker, null=True, blank=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         if self.user:
#             return self.user.username
#         else:
#             return 'UserProfile with no associated User'
        
