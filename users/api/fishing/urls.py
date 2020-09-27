from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('fish-create/', views.fish_create, name="fish-create"),
    path('fish-list/', views.fish_list, name="fish-list"),
    path('fish-list/<str:fish>/', views.fish_detail, name="fish-detail"),
    path('fish-update/<str:fish>/', views.fish_update, name="fish-update"),
    path('user-list/', views.user_list, name="user-list"),
    path('user-list/<str:user>/', views.user_fishes, name="user-fishes"),
    path('user-profile/<str:user>/', views.user_profile, name="user-profile"),
    path('profile-list/', views.profile_list, name="profile-list"),
    path('profile-list/<str:id>/', views.profile_detail, name="profile-detail"),
    path('profile-update/<str:user>/', views.profile_update, name="profile-update"),
]
