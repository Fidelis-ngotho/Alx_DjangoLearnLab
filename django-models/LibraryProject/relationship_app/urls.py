from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import your views module

urlpatterns = [
    # Login view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Register view
    path('register/', views.register, name='register'),
]
