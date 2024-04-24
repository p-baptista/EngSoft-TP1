from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpRequest, HttpResponseRedirect
from main_app.models import *
from main_app.forms import *


class LoginView(ListView):
    template_name = "login_page.html"
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        error = self.request.GET.get('error')
        if error:
            context['error'] = error
            
        return context
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')).last()
        
        if user:
            user.is_authenticated = True
            user.save()
            
            return HttpResponseRedirect(f'/{user.username}')
        else:
            return HttpResponseRedirect('/login' + '?error=Usuário e/ou senha não encontrados')
    
class SignupView(CreateView):
    template_name = "signup.html"
    fields = ['username', 'email', 'password']
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        error = self.request.GET.get('error')
        if error:
            context['error'] = error
        
        return context
    
    def post(self, request, *args, **kwargs):
        
        password = request.POST['password']
        if password != request.POST['confirm_password']:
            return HttpResponseRedirect('/signup' + '?error=As senhas informadas não coincidem')
        
        username = request.POST['username']
        if User.objects.filter(username=username):
            return HttpResponseRedirect('/signup' + '?error=O username ja está sendo utilizado')
        
        user_data = {
            "username":username,
            "password":password,
            "email":request.POST['email'],
            "is_authenticated":False
        }
        
        new_user = User(**user_data)
        new_user.save()
        
        return HttpResponseRedirect("/login")
        
        
class HeaderView(ListView):
    template_name="header.html"
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        
        if user:
            context['user'] = user
            
            context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1__username = user.username)]
            
        return context

class HomeView(ListView):
    template_name="home.html"
    model = User
    
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        if user.is_authenticated == False:
            return HttpResponseRedirect('/login' + '?error=Faça o login para entrar no app')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        if user.is_authenticated == False:
            return HttpResponseRedirect('/login' + '?error=Faça o login para entrar no app')
        
        if user:
            context['user'] = user

            context['user_games'] = [review.game for review in Review.objects.filter(user__username = user.username)]
            
            context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1__username = user.username)]
            
            context['user_reviews'] = Review.objects.filter(user_id=user.id)

            search_game_name = self.request.GET.get('searched')     
            if search_game_name:
                context['game_query'] = Game.objects.filter(name__contains=self.request.GET.get('searched'))

            search_friend_name = self.request.GET.get('searched_friend')     
            if search_friend_name:
                context['friend_query'] = User.objects.filter(username__contains=self.request.GET.get('searched_friend'))

        return context
    
class ProfileView(ListView):
    template_name="profile.html"
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        friend = User.objects.filter(username=self.request.resolver_match.kwargs['friend']).last()

        if user and friend:
            context['user'] = user

            context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1__username = user.username)]

            context['friend'] = friend
            
            context['friend_reviews'] = Review.objects.filter(user_id=friend.id)

            context['games_reviewed'] = len(Review.objects.filter(user_id=friend.id))
            
        return context

    
class GameReviewView(ListView):
    template_name="game_review.html"
    model = Review 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_name = self.request.resolver_match.kwargs['gamename']
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        context['user'] = user
        
        context['game'] = Game.objects.filter(name=game_name).last()
        
        context['user_review'] = Review.objects.filter(game__name=game_name, user_id=user.id).last()
        
        user_friends_id = [friendship.user2.id for friendship in FriendList.objects.filter(user1_id=user.id)]
        context['user_friends'] = User.objects.filter(id__in=user_friends_id)
        
        context['friends_review'] = Review.objects.filter(game__name=game_name, user_id__in=user_friends_id)

        return context
    
    
class AddGameReviewView(CreateView):
    template_name="add_game_review.html"
    model = Review
    fields = ['platform', 'comment', 'rating']
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        game = Game.objects.filter(name=self.request.resolver_match.kwargs['gamename']).last()
        
        review = Review.objects.filter(
            game__name=game.name,
            user_id=user.id
        ).last()
        
        new_game_rating = int(request.POST.get('game_rating'))
        
        platform_id = request.POST.get('platform')
        platform_instance = Platform.objects.get(id=platform_id)
        
        if review:
            old_game_rating = review.rating
            
            number_of_reviews = Review.objects.filter(game__name=game.name).count()
            new_mean_rating = (((game.mean_rating * number_of_reviews) - old_game_rating) + new_game_rating) / number_of_reviews
            
            game.mean_rating = new_mean_rating
            game.save()
            
            review.comment = request.POST.get('comment')
            review.rating = new_game_rating
            review.platform = platform_instance
            
            review.save()
            
            redirect_url = reverse('review-game', kwargs={'username': user.username, 'gamename': game.name})
            return redirect(redirect_url)
        
        if game.mean_rating:
            new_mean = (game.mean_rating + new_game_rating)/2
            game.mean_rating = new_mean
        else:
            game.mean_rating = new_game_rating
            
        game.save()
            
        review_data = {
            "user": user,
            "game": game,
            "platform": platform_instance,
            "comment": request.POST.get('comment'),
            "date": datetime.now(),
            "rating": new_game_rating,
        }
        
        new_review = Review(**review_data)
        new_review.save()
        
        redirect_url = reverse('review-game', kwargs={'username': user.username, 'gamename': game.name})
        return redirect(redirect_url)
        
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        game_name = self.request.resolver_match.kwargs['gamename']
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        context['user'] = user
        
        context['user_review'] = Review.objects.filter(game__name=game_name, user_id=user.id).last()
        
        context['game'] = Game.objects.filter(name=game_name).last()
        
        context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1_id=user.id)]

        return context    
    
class ResetPasswordView(ListView):
    template_name = "reset_password.html"
    model = User
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     error = self.request.GET.get('error')
    #     if error:
    #         context['error'] = error
            
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     user = User.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')).last()
        
    #     if user:
    #         user.is_authenticated = True
    #         user.save()
            
    #         return HttpResponseRedirect(f'/{user.username}')
    #     else:
    #         return HttpResponseRedirect('/login' + '?error=Usuário e/ou senha não encontrados')

class GameSearchView(ListView):
    template_name="games.html"
    model = User
    
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        if user.is_authenticated == False:
            return HttpResponseRedirect('/login' + '?error=Faça o login para entrar no app')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = User.objects.filter(username=self.request.resolver_match.kwargs['username']).last()
        if user.is_authenticated == False:
            return HttpResponseRedirect('/login' + '?error=Faça o login para entrar no app')
        
        if user:
            context['user'] = user

            context['user_games'] = [review.game for review in Review.objects.filter(user__username = user.username)]
            
            context['user_friends'] = [friendship.user2 for friendship in FriendList.objects.filter(user1__username = user.username)]
            
            context['user_reviews'] = Review.objects.filter(user_id=user.id)

            search_game_name = self.request.GET.get('searched')     
            if search_game_name:
                context['game_query'] = Game.objects.filter(name__contains=self.request.GET.get('searched'))

        return context