from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-timesheet/', views.submit_timesheet, name='submit_timesheet'),
    path('timesheets/', views.timesheet_list, name='timesheet_list'),
    path('timesheets/<int:pk>/', views.timesheet_detail, name='timesheet_detail'),
]
