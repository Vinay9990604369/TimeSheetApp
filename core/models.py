from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f"{self.resource.username} - {self.project_name} - {self.date_of_services}"
