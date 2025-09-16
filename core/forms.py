from django import forms
from .models import Account, Category, Transaction, SavingGoal

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'balance']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'category', 'amount', 'transaction_type', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class SavingGoalForm(forms.ModelForm):
    class Meta:
        model = SavingGoal
        fields = ['name', 'target_amount', 'current_amount']
