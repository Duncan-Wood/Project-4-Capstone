from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import User


#put steps on the shelf for now
class Step(models.Model):
    step = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.step

class UserStep(models.Model):
    USER_STEP_STATUS_CHOICES = (
        (0, 'Incomplete'),
        (1, 'Complete'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_steps', null=True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='step_usersteps', null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.IntegerField(choices=USER_STEP_STATUS_CHOICES, default=0)
    completed_at = models.DateTimeField(null=True, blank=True)  # Add completed_at field

    def __str__(self):
        return self.step.step

class UserAddiction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_addictions', null=True)
    addiction = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.addiction} test '

class TimeTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_trackers', null=True)
    user_addiction = models.ForeignKey(UserAddiction, null=True, blank=True, on_delete=models.SET_NULL)  # Add ForeignKey for UserAddiction
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(default = datetime.timedelta(0))
    money_tracker = models.OneToOneField('MoneyTracker', null=True, blank=True, on_delete=models.SET_NULL)  # Add OneToOneField for MoneyTracker

    def __str__(self):
        return f'TimeTracker for {self.user_addiction}'
    
# money tracker model to store the amount of money tracker by the user based on the duration of the time tracker
class MoneyTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='money_trackers', null=True)
    time_tracker = models.OneToOneField(TimeTracker, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f'MoneyTracker for {self.user}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_step = models.ForeignKey(UserStep, null=True, blank=True, on_delete=models.SET_NULL)
    user_addiction = models.ForeignKey(UserAddiction, null=True, blank=True, on_delete=models.SET_NULL)
    time_tracker = models.ForeignKey(TimeTracker, null=True, blank=True, on_delete=models.SET_NULL)
    money_tracker = models.ForeignKey(MoneyTracker, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return 'UserProfile with no associated User'
        
class Token(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tokens')
    name = models.CharField(max_length=150)
    description = models.TextField()
    earned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name