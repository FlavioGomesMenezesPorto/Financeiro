from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Account, Category, Transaction, SavingGoal
from .forms import AccountForm, CategoryForm, TransactionForm, SavingGoalForm

@login_required
def dashboard(request):
    accounts = Account.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(user=request.user)
    saving_goals = SavingGoal.objects.filter(user=request.user)

    context = {
        'accounts': accounts,
        'categories': categories,
        'transactions': transactions,
        'saving_goals': saving_goals,
    }

    return render(request, 'core/dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('dashboard')
    else:
        form = AccountForm()
    return render(request, 'core/add_account.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('dashboard')
    else:
        form = CategoryForm()
    return render(request, 'core/add_category.html', {'form': form})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
        form.fields['account'].queryset = Account.objects.filter(user=request.user)
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'core/add_transaction.html', {'form': form})

@login_required
def add_saving_goal(request):
    if request.method == 'POST':
        form = SavingGoalForm(request.POST)
        if form.is_valid():
            saving_goal = form.save(commit=False)
            saving_goal.user = request.user
            saving_goal.save()
            return redirect('dashboard')
    else:
        form = SavingGoalForm()
    return render(request, 'core/add_saving_goal.html', {'form': form})
