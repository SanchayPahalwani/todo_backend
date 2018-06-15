from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField('due date')
    complete = models.BooleanField(default=False)
    parent = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
