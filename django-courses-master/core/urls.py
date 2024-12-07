from django.urls import path
from . import views


urlpatterns = [
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/update-profile/', views.update_profile, name="update-profile"),
    path('accounts/save-profile/', views.save_profile, name="save-profile"),
]
