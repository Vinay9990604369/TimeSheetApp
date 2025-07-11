from django import forms
from .models import TimeSheetEntry

class TimeSheetEntryForm(forms.ModelForm):
    class Meta:
        model = TimeSheetEntry
        fields = [
            'supplier_name',
            'customer',
            'project_name',
            'project_id',
            'service_type_id',
            'phase',
            'task_id',
            'date_of_services',
            'duration',
            'work_description',
        ]
        widgets = {
            'date_of_services': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.TimeInput(attrs={'type': 'time'}),
        }
