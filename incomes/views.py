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
    model = Incomes
    template_name = 'incomes/incomes.html'
    ordering = ['-date_added']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the categories
        context['incomes_list'] = Incomes.objects.filter(user=self.request.user)
        return context

    def get_queryset(self):
        return Incomes.objects.order_by('-date_added')


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


class AddIncomeView(LoginRequiredMixin, CreateView):
    login_url = 'accounts/login/'
    model = Incomes
    form_class = IncomesForm
    template_name = 'incomes/add_income.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # messages.success(self.request, 'Expense added successfully.')
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super(AddIncomeView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    success_url = reverse_lazy('incomes')


class EditIncomeView(UpdateView):
    model = Incomes
    fields = ['income_name', 'amount', 'source', 'date_added']
    template_name = 'incomes/edit_income.html'
    success_url = reverse_lazy('incomes')


class DeleteIncomeView(DeleteView):
    model = Incomes
    template_name = 'incomes/delete_income.html'
    success_url = reverse_lazy('incomes')


def search_income(request):
    if request.method == 'POST':
        searched_str = json.loads(request.body).get('searchedText')

        incomes = Incomes.objects.filter(
            amount__istartswith=searched_str,
            user=request.user) | Incomes.objects.filter(
            expense_name__icontains=searched_str,
            user=request.user) | Incomes.objects.filter(
            date_added__istartswith=searched_str,
            user=request.user) | Incomes.objects.filter(
            source__source_name__icontains=str(searched_str),
            user=request.user).select_related('source_name')

        e = list(incomes.values('source_id'))
        # print(type(e))
        try:
            ex = e[0]
            # print(ex)
        except IndexError:
            ex = {}

        source_id = ex.get('source_id')
        # print(ex.get('category_id'))
        # from operator import itemgetter
        # x = (map(itemgetter('category_id'),e))
        # print(x)
        # for
        # print(list(expenses[0]["category_id"]))
        #don't touch
        data = list(incomes.values())
        # print(data)
        res =[]
        for c in data:
            c["source_name"] = str(Source.objects.get(id=source_id))
            res.append(c)
            print(res)

        return JsonResponse(res, safe=False)
