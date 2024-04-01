from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("<str:username>/", views.HomeView.as_view(), name="home"),
    path("search-game/", views.SearchGameView.as_view(), name="search-game"),
    path("review-page/<str:name>", views.GameReviewView.as_view(), name="review-game"),
    path("add-review/<str:name>", views.AddGameReviewView.as_view(), name="add-game-review"),
    path("friend-list/<str:username>", views.FriendListView.as_view(), name="friend-list")
]