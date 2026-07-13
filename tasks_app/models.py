# Create your models here.
from django.db import models
from django.utils import timezone

class DailyTask(models.Model):
    task_name = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    @property
    def credit_value(self):
        # High priority: Finance (25)
        if 'Finance' in self.task_name: return 25
        # Medium priority: Build (20)
        if 'Build' in self.task_name: return 20
        # Default: Flex (10)
        return 10

    def __str__(self):
        return self.task_name
    
# Add this to your existing models.py
class FlexTask(models.Model):
    task_name = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    @property
    def credit_value(self):
        return 10 # Flex tasks are always 10