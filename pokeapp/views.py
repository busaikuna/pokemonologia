from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Card, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def add_card(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        foto = request.FILES.get('image')
        descricao = request.POST.get('description')
        ataque = request.POST.get('atk')
        defesa = request.POST.get('def')
        hp = request.POST.get('hp')
        classe = "Comunidade"

        card = Card(
            user=request.user,
            nome=nome,
            foto=foto,
            descricao=descricao,
            ataque=ataque,
            defesa=defesa,
            hp=hp,
            classe=classe,
        )
        card.save()
        return redirect('Pokemonologia')

    return render(request, 'pokeapp/add_card.html')

def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        profile = Profile(user=user)
        profile.save()
        redirect('pokeapp/login.html')

    return render(request, 'pokeapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Pokemonologia')
        else:
            messages.error(request, 'Username ou senha incorretos.')
    
    return render(request, 'pokeapp/login.html')

@login_required
def pokemonologia(request):
    cards = Card.objects.all()
    return render(request, 'pokeapp/pokemonologia.html', {"cards": cards})

@login_required
def comunidade(request):
    cards = Card.objects.all()
    return render(request, 'pokeapp/comunidade.html', {"cards": cards})