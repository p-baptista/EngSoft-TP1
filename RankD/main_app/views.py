from django.shortcuts import render
from django.views.generic import ListView, CreateView
from main_app.models import *

# Create your views here.
class LoginView(ListView):
    template_name = "login_page.html"
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
class HomeView(ListView):
    template_name="home.html"
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchGameView(ListView):
    template_name="search_game.html"
    model = Game
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class GameReviewView(ListView):
    template_name="game_review.html"
    model = Review 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['user_review'] = Review.objects.filter(user__username='cesar', game__name='zelda').last()
        context['other_reviews'] = Review.objects.filter(game__name='zelda')
        
        return context
    
class AddGameReviewView(CreateView):
    template_name="add_game_review.html"
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class FriendListView(ListView):
    template_name="friend_list.html"
    model = FriendList  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  