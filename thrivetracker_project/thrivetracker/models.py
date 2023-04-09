from django.db import models
from django.conf import settings
import datetime

class Step(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserStep(models.Model):
    USER_STEP_STATUS_CHOICES = (
        (0, 'Incomplete'),
        (1, 'Complete'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_steps', null=True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='step_usersteps', null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.IntegerField(choices=USER_STEP_STATUS_CHOICES, default=0)
    swap_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='swap_step_usersteps', null=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)  # Add completed_at field

    def __str__(self):
        return self.step.name

    def swap_steps(self, new_step_id):
        # Method to swap the step with a new step by updating swap_step field
        self.swap_step = self.step
        self.step = Step.objects.get(id=new_step_id)
        self.save()

    def undo_swap(self):
        # Method to undo the step swap by reverting back to the original step
        if self.swap_step:
            self.step, self.swap_step = self.swap_step, None
            self.save()

class TimeTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='time_trackers', null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # recommended to calculate the duration in the viewor serializer and store it in a separate field

    def __str__(self):
        return str(self.end_time - self.start_time)

class UserAddiction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_addictions', null=True)
    name = models.CharField(verbose_name='Addiction Name', max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# money tracker model to store the amount of money tracker by the user based on the duration of the time tracker
class MoneyTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='money_trackers', null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} {self.currency} on {self.date}"