from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TimeSheetEntry(models.Model):
    resource = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    project_id = models.CharField(max_length=100)
    service_type_id = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    task_id = models.CharField(max_length=100, blank=True, null=True)
    date_of_services = models.DateField()
    duration = models.TimeField()
    work_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resource.username} - {self.project_name} - {self.date_of_services}"

    class Meta:
        verbose_name = "Time Sheet Entry"
        verbose_name_plural = "Time Sheet Entries"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('consultant', 'Consultant'),
        ('client', 'Client'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    organization = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
