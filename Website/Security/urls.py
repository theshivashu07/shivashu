from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('index',views.index,name='index'),

    path("", views.index, name="security"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("logout/confirmations/", views.logout_confirmations, name="logout_confirmations"),
    # path('signup/', views.signup_view, name='signup'),
    path('signup/', views.register_view, name='signup'),
    path("register/", views.register_view, name="register"),
    path("reset-password/", views.reset_password, name="reset_password"),

    path("profile-setup/", views.profile_setup, name="profile_setup"),

    path("refresh/", views.refresh_token_view, name="refresh_token"),


]

