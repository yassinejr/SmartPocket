from django.shortcuts import render



# Create your views here.

def index(request):
    return render(request, 'expenses/expenses.html')


def add_expense(request):
    return render(request, 'expenses/add_expense.html')
