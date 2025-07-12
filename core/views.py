from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TimeSheetEntryForm
from .models import UserProfile, TimeSheetEntry
from django.contrib import messages  # <-- Keep this import

@login_required
def home(request):
    # Home page, shows basic info and links
    return render(request, 'core/home.html', {'user': request.user})

@login_required
def submit_timesheet(request):
    profile = request.user.userprofile
    
    # Only consultants can submit timesheets
    if profile.role != 'consultant':
        messages.error(request, "❌ You are not authorized to submit timesheets.")
        return redirect('home')

    if request.method == 'POST':
        form = TimeSheetEntryForm(request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.resource = request.user  # Assign current user as resource
            timesheet.save()
            messages.success(request, "✅ Timesheet submitted successfully!")
            return redirect('home')  # Redirect after successful save
        else:
            messages.error(request, "⚠️ There was an error with your submission. Please check the form.")
    else:
        form = TimeSheetEntryForm()

    return render(request, 'core/timesheet_form.html', {'form': form})

@login_required
def timesheet_list(request):
    profile = request.user.userprofile
    
    if profile.role == 'admin':
        # Admin sees all timesheets
        timesheets = TimeSheetEntry.objects.all().order_by('-date_of_services')
    else:
        # Consultants and others see only their own timesheets
        timesheets = TimeSheetEntry.objects.filter(resource=request.user).order_by('-date_of_services')
    
    return render(request, 'core/timesheet_list.html', {'timesheets': timesheets})

@login_required
def timesheet_detail(request, pk):
    timesheet = get_object_or_404(TimeSheetEntry, pk=pk)
    profile = request.user.userprofile

    # Admins can see all, others only their own timesheets
    if profile.role != 'admin' and timesheet.resource != request.user:
        messages.error(request, "❌ You are not authorized to view this timesheet.")
        return redirect('timesheet_list')  # No access if unauthorized
    
    return render(request, 'core/timesheet_detail.html', {'timesheet': timesheet})
