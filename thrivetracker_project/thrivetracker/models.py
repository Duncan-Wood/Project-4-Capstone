from django.db import models
from django.conf import settings
import datetime

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
        return self.step.name

    # def swap_steps(self, new_step_id):
    #     # Method to swap the step with a new step by updating swap_step field
    #     self.swap_step = self.step
    #     self.step = Step.objects.get(id=new_step_id)
    #     self.save()

    # def undo_swap(self):
    #     # Method to undo the step swap by reverting back to the original step
    #     if self.swap_step:
    #         self.step, self.swap_step = self.swap_step, None
    #         self.save()

class UserAddiction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_addictions', null=True)
    addiction = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.addiction

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
        try:
            return f'MoneyTracker {self.pk} for User {self.user.username} and TimeTracker {self.time_tracker.user_addiction}'
        except TimeTracker.DoesNotExist:
            return f'MoneyTracker {self.pk} for User {self.user.username}'
