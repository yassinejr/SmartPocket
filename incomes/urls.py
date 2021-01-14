from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('incomes', views.IndexView.as_view(), name="incomes"),
    path('add_income', views.AddIncomeView.as_view(), name="add_income"),
    path('edit_income/<int:pk>', views.EditIncomeView.as_view(), name="edit_income"),
    path('delete_income/<int:pk>', views.DeleteIncomeView.as_view(), name="delete_income"),
    path('search_incomes', csrf_exempt(views.search_income), name="search_incomes"),
]