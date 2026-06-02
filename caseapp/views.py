from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def shots(request):
    return render(request, 'shots.html')

def designers(request):
    return render(request, 'designers.html')

def teams(request):
    return render(request, 'teams.html')

def community(request):
    return render(request, 'community.html')

def designs(request):
    return render(request, 'designs.html')

def signup(request):
    return render(request, 'signup.html')