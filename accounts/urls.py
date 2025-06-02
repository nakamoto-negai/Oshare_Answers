from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('signout/', views.signout_view, name='signout'),
    path('login/', views.signin_view, name='login'),
    path('profile/<int:user_id>/', views.profile, name='profile'),

]