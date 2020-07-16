from django.contrib.auth.models import User
from django.db import models


# Create your models here.
STATUS = [
    ('TD', 'ToDo'),
    ('P', 'Progress'),
    ('R', 'Review'),
    ('D', 'Done'),
]


class Project(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=245, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default='TD')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
    


