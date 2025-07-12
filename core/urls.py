from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_timesheet/', views.submit_timesheet, name='submit_timesheet'),
    path('timesheet_list/', views.timesheet_list, name='timesheet_list'),
    path('timesheet/<int:pk>/', views.timesheet_detail, name='timesheet_detail'),
]
