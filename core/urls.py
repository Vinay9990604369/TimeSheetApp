from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-timesheet/', views.submit_timesheet, name='submit_timesheet'),
]
