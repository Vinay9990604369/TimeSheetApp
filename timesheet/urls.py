from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import home  # Import the home view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),  # Root path now handled
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
