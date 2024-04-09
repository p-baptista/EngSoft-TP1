from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("<str:username>/", views.HomeView.as_view(), name="home"),
    path("<str:username>/review-page/<str:gamename>", views.GameReviewView.as_view(), name="review-game"),
    path("<str:username>/add-review/<str:gamename>", views.AddGameReviewView.as_view(), name="add-game-review"),
]