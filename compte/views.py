from django.contrib.messages import get_messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import UserUpdateForm, UserCreationForm


def register(request):
    context = {
        'page_title': 'Register',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nom utilisateur déjà existant! Essayez un autre...')
                return HttpResponseRedirect(reverse('compte:register'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Compte ajouté avec succès!..')
                return HttpResponseRedirect(reverse('compte:login'))
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas!..')
            return HttpResponseRedirect(reverse('compte:register'))
    else:
        return render(request, 'compte/register.html', context)


def login(request):
    context = {
        'page_title': 'Login',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('Connexion réussie: ', username)
            return HttpResponseRedirect(reverse('application:home'))
        else:
            messages.error(request, 'Utilisateur ou mot de passe incorrect')
            messages.get_messages(request).used = True
            return HttpResponseRedirect(reverse('compte:login'))
    else:
        return render(request, 'compte/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages = get_messages(request)
        for msg in messages:
            pass

            del msg
        return HttpResponseRedirect(reverse('compte:login'))


@login_required(login_url='home')
def profile(request, username):
    account = get_object_or_404(User, username=username)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=account)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Mise à jour du compte réussie!')
            return HttpResponseRedirect(reverse('application:home'))
    else:
        u_form = UserUpdateForm(instance=account)

    context = {
        'u_form': u_form,
        'account': account
    }
    return render(request, 'compte/profile.html', context)


@login_required(login_url='home')
def index(request):
    return HttpResponseRedirect(reverse('application:home'))

@login_required(login_url='home')
def deleteProfile(request, username):
    account = get_object_or_404(User, username=username)
    if request.method == 'POST':
        account.delete()
        messages.success(request, 'Profil supprimé avec succès!')
        return redirect('compte:login')
    return render(request, 'compte/deleteProfile.html', {'account': account})


@login_required(login_url='home')
def deleteProfileClassique(request, username):
    account = get_object_or_404(User, username=username)
    if request.method == 'POST':
        account.delete()
        messages.success(request, 'Profil supprimé avec succès!')
        return redirect('compte:user_list')
    return render(request, 'compte/deleteProfile.html', {'account': account})


@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    return render(request, 'compte/user_list.html', {'users': users})



