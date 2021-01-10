from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *


# Create your views here.
class IndexView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['expenses_list'] = Expenses.objects.filter(user=self.request.user)
        return context

    def get_queryset(self):
        return Expenses.objects.order_by('-date_added')


# def index(request):
#     expenses = Expenses.objects.filter(user=request.user)
#     context = {'expenses': expenses}
#     return render(request, 'expenses/expenses.html', context)


# def add_expense(request):
#     context = {}
#     if request.method == 'POST':
#         form = ExpensesForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#         else:
#             form = ExpensesForm()
#     context['form'] = ExpensesForm()
#     print(context)
#     messages.add_message(request, messages.SUCCESS, 'Expense added successfully')
#     return render(request, 'expenses/add_expense.html', context)


class AddExpenseView(LoginRequiredMixin, CreateView):
    login_url = 'accounts/login/'
    model = Expenses
    form_class = ExpensesForm
    template_name = 'expenses/add_expense.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # messages.success(self.request, 'Expense added successfully.')
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(AddExpenseView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    success_url = reverse_lazy('expenses')


class EditExpenseView(UpdateView):
    model = Expenses
    fields = '__all__'
    template_name = 'expenses/delete_expense.html'
    success_url = reverse_lazy('expenses')


class DeleteExpenseView(DeleteView):
    model = Expenses
    template_name = 'expenses/delete_expense.html'
    success_url = reverse_lazy('expenses')


