from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('signup/', views.signup, name='signup'),
]