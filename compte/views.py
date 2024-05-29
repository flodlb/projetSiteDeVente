from django.shortcuts import render, get_object_or_404
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import  UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,f'Nom utilisateur deja existant! essayez un autre...')
                return HttpResponseRedirect(reverse('compte :register'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request,f'Compte ajouté avec succès!..')
                return HttpResponseRedirect(reverse('account:login'))
        else:
            messages.error(request,f'Mauvais mot de passe!..')
            return HttpResponseRedirect(reverse('compte:register'))
    else:
        return render(request, 'compte/register.html')
    
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'connection ok')
            return HttpResponseRedirect(reverse('application:home'))
        else:
            messages.error(request,f'utilisateur ou mot de passe mauvais')
            return HttpResponseRedirect(reverse('compte:login'))
    else:
        return render(request, 'compte/login.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,f'Deconnection en cours...')
        return HttpResponseRedirect(reverse('compte:login'))

@login_required(login_url='home')
def profile(request, pk):
    context={}
    account = get_object_or_404(User, id = pk)
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=account)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=account.profile)
        if u_form.is_valid( ) and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Mise à jour du compte OK!')
            return HttpResponseRedirect(reverse('compte:index'))
        
        else:
            u_form = UserUpdateForm(instance=account)
            p_form = ProfileUpdateForm(instance=account.profile)
            
        context = {
            'u_form' : u_form,
            'p_form': p_form,
            'account' : account
        }
        return render(request, 'compte/profile.html',context)
    
@login_required(login_url='home')
def index(request):
    context={}
    context["compte_liste"] = User.objects.all
    return render(request, "compte/index.html", context)