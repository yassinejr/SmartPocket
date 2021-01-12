from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import JsonResponse

from .forms import *


# Create your views here.
class IndexView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    ordering = ['-date_added']
    paginate_by = 3

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
    fields = ['expense_name', 'amount', 'category', 'date_added']
    template_name = 'expenses/edit_expense.html'
    success_url = reverse_lazy('expenses')


class DeleteExpenseView(DeleteView):
    model = Expenses
    template_name = 'expenses/delete_expense.html'
    success_url = reverse_lazy('expenses')


def search_expense(request):
    if request.method == 'POST':
        searched_str = json.loads(request.body).get('searchedText')

        expenses = Expenses.objects.filter(
            amount__istartswith=searched_str,
            user=request.user) | Expenses.objects.filter(
            expense_name__icontains=searched_str,
            user=request.user) | Expenses.objects.filter(
            date_added__istartswith=searched_str,
            user=request.user) | Expenses.objects.filter(
            category__category_name__icontains=str(searched_str),
            user=request.user).select_related('category_name')


        # cat = Category.objects.filter(category_name=searched_str, user=request.user).values()

        e = list(expenses.values('category_id'))
        # print(e[0])
        ex = e[0]
        cat_id = ex.get('category_id')
        print(ex.get('category_id'))
        # from operator import itemgetter
        # x = (map(itemgetter('category_id'),e))
        # print(x)
        # for
        # print(list(expenses[0]["category_id"]))
        #don't touch
        data = list(expenses.values())
        # print(data)
        res =[]
        for c in data:
            c["category_name"] = str(Category.objects.get(id=cat_id))
            res.append(c)
            print(res)

        return JsonResponse(res, safe=False)
