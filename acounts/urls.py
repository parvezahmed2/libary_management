from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLgoutView, UserProfileView, UserAccountUpdateView  
urlpatterns = [
    
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',UserLgoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    path('profile_update/',UserAccountUpdateView.as_view(), name='update_profile'),

]