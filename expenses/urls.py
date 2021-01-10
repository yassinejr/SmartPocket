from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="expenses"),
    path('add_expense', views.AddExpenseView.as_view(), name="add_expenses"),
    path('edit_expense/<int:pk>', views.EditExpenseView.as_view(), name="edit_expense"),
    path('delete_expense/<int:pk>', views.DeleteExpenseView.as_view(), name="delete_expense"),
]
