from django.shortcuts import render
from django.views.generic import ListView, CreateView
from main_app.models import *
from main_app.forms import *

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
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        context['user'] = user
        
        context['user_games'] = [review.game for review in Review.objects.filter(user_id=user.id)]
         
        context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1_id=user.id)]
        
        context['user_reviews'] = Review.objects.filter(user_id=user.id)
        
        return context

    
class GameReviewView(ListView):
    template_name="game_review.html"
    model = Review 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_name = self.request.resolver_match.kwargs['gamename']
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        context['user'] = user
        
        context['game'] = Game.objects.filter(name=game_name)
        
        context['user_review'] = Review.objects.filter(game__name=game_name, user_id=user.id).last()
        
        user_friends_id = [friendship.user2.id for friendship in FriendList.objects.filter(user1_id=user.id)]
        context['user_friends'] = User.objects.filter(id__in=user_friends_id)
        
        context['friends_review'] = Review.objects.filter(game__name=game_name, user_id__in=user_friends_id)
        
        return context
    
    
class AddGameReviewView(CreateView):
    template_name="add_game_review.html"
    model = Review
    fields = ['platform', 'comment', 'rating']
    form = AddReviewForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_name = self.request.resolver_match.kwargs['gamename']
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        context['user'] = user
        
        context['game'] = Game.objects.filter(name=game_name)
        
        context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1_id=user.id)]

        return context    