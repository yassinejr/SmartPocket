from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View


# Create your views here.
# class IndexView(ListView):
#     template_name = 'dashboard/base.html'
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)