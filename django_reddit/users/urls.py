"""Users urls"""

# Django
from django.urls import path

# Views
from . import views

app_name = 'users'
urlpatterns = [
    # User
    path('p/<str:username>/', views.UserDetailView.as_view(), name="detail"),

    # Management
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update_profile'),
]