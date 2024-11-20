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


from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
urlpatterns = [
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
]

