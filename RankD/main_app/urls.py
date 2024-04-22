from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("reset_password/", views.ResetPasswordView.as_view(), name="reset_password"),
    path("<str:username>/", views.HomeView.as_view(), name="home"),
    path("profile/<str:username>/", views.ProfileView.as_view(), name="profile"),
    path("<str:username>/review-page/<str:gamename>", views.GameReviewView.as_view(), name="review-game"),
    path("<str:username>/add-review/<str:gamename>", views.AddGameReviewView.as_view(), name="add-game-review"),
]