from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import InscriptionForm
from .models import Profile

def inscription(request):
    if request.user.is_authenticated:
        return redirect('accueil')

    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, telephone=form.cleaned_data['telephone'])
            login(request, user)
            messages.success(request, "Bienvenue ! Ton compte a été créé.")
            return redirect('accueil')
    else:
        form = InscriptionForm()

    return render(request, 'registration/signup.html', {'form': form})