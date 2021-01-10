from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add_expense', views.AddExpenseView.as_view(), name="add_expenses"),
]
