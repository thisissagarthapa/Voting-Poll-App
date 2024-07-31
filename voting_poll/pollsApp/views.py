from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Question,Option

# Create your views here.
def home(request):
    return render(request,'home.html')

# views.py
@login_required(login_url='log_in')
def result(request):
    questions = Question.objects.all()
    for question in questions:
        total_votes = question.total_votes
        for option in question.options.all():
            if total_votes > 0:
                option.percentage = (option.votes / total_votes) * 100
            else:
                option.percentage = 0
    return render(request, 'result.html', {'questions': questions})



@login_required(login_url='log_in')
def vote(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        option_id = request.POST.get('candidate_vote') 
        option = get_object_or_404(Option, pk=option_id)
        option.votes += 1  # Increment the vote count
        option.save()  # Save the updated vote count
        return redirect('result')  # Redirect to the result page after voting
    return render(request, 'vote.html', {'questions': questions})


@login_required(login_url='log_in')
def dashboard(request):
    return render(request, 'dashboard.html')



def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, f"Hello {name}, your username already exists.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, f"Hello {name}, your email already exists.")
                return redirect('register')
            else:
                User.objects.create_user(first_name=name, username=username, email=email, password=password)
                messages.success(request, f"Hello {name}, you have registered successfully.")
                return redirect('log_in')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username not found.")
            return redirect('log_in')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'auth/login.html')


@login_required(login_url='log_in')
def log_out(request):
    logout(request)
    return redirect('home')
