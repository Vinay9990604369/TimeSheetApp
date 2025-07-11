from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TimeSheetEntryForm
from .models import UserProfile

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
