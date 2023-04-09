from django.db import models
from django.conf import settings
import datetime
# from django.contrib.auth.models import AbstractUser

class Step(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

# # redefine the User model to remove unnecessary fields    
# class User(AbstractUser):
#     # Removing the first_name and last_name fields from the User model could cause issues with the Django admin site and authentication
#     # first_name = None
#     # last_name = None
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.TextField()

#     def __str__(self):
#         return self.name
    
class UserStep(models.Model):
    USER_STEP_STATUS_CHOICES = (
        (0, 'Incomplete'),
        (1, 'Complete'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usersteps', null=True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='step_usersteps', null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.IntegerField(choices=USER_STEP_STATUS_CHOICES, default=0)
    swap_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='swap_step_usersteps', null=True)

    def __str__(self):
        return self.step.name

    def swap_steps(self, new_step_id):
        # Method to swap the step with a new step by updating swap_step field
        self.swap_step = self.step  # Store the current step in swap_step
        self.step = Step.objects.get(id=new_step_id)  # Update the step field with the new step
        self.save()

    def undo_swap(self):
        # Method to undo the step swap by reverting back to the original step
        if self.swap_step:
            self.step, self.swap_step = self.swap_step, None  # Swap back the steps
            self.save()

class TimeTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='timetrackers', null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # recommended to calculate the duration in the viewor serializer and store it in a separate field

    def __str__(self):
        return str(self.end_time - self.start_time)

class UserAddiction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='useraddictions', null=True)
    name = models.CharField(verbose_name='Addiction Name', max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# money saved model to store the amount of money saved by the user based on the duration of the time tracker
class MoneySaved(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='money_saved', null=True)
    duration = models.IntegerField(verbose_name='Duration (days)', help_text='Duration in days based on the time tracker', null=True, default=0)
    amount = models.IntegerField(verbose_name='Amount saved', help_text='Amount of money saved based on the duration', null=True, default=0)
    time_tracker = models.OneToOneField(TimeTracker, on_delete=models.CASCADE, related_name='money_saved', null=True)

    def __str__(self):
        return f"Amount saved: ${self.amount} for {self.duration} days"
