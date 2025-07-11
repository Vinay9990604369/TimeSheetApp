from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TimeSheetEntryForm
from .models import UserProfile, TimeSheetEntry

@login_required
def home(request):
    return render(request, 'core/home.html', {'user': request.user})

@login_required
def submit_timesheet(request):
    profile = request.user.userprofile
    if profile.role != 'consultant':
        # Optionally, add a message here explaining why
        return redirect('home')  # Only consultants allowed to submit timesheets

    if request.method == 'POST':
        form = TimeSheetEntryForm(request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.resource = request.user  # Assign current user as resource
            timesheet.save()
            return redirect('home')  # Redirect after successful save
    else:
        form = TimeSheetEntryForm()

    return render(request, 'core/timesheet_form.html', {'form': form})

@login_required
def timesheet_list(request):
    profile = request.user.userprofile
    if profile.role == 'admin':
        timesheets = TimeSheetEntry.objects.all().order_by('-date_of_services')
    else:
        # For consultants and others, show only their timesheets
        timesheets = TimeSheetEntry.objects.filter(resource=request.user).order_by('-date_of_services')
    
    return render(request, 'core/timesheet_list.html', {'timesheets': timesheets})

@login_required
def timesheet_detail(request, pk):
    timesheet = get_object_or_404(TimeSheetEntry, pk=pk)
    # Check if user has access:
    if request.user.userprofile.role != 'admin' and timesheet.resource != request.user:
        return redirect('timesheet_list')  # No access if not admin or owner
    
    return render(request, 'core/timesheet_detail.html', {'timesheet': timesheet})
