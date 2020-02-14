from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import ExpensesCategoryForm, ExpensesForm
from .models import Expenses, ExpensesCategory


class ExpensesCategoryView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'expenses_category.html'

    def get(self, request):
        context = {
            'form': ExpensesCategoryForm,
            'category': ExpensesCategory.objects.filter(user_id=request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ExpensesCategoryForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "Category added Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Category creation Failed")
            return redirect('expenses_category')


class ExpensesAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'add_expenses.html'

    def get(self, request):
        context = {
            'form': ExpensesForm
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Expenses Created Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Expenses creation Failed")
            return redirect('expenses_create')


class ExpensesView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'expenses.html'

    def get(self, request):
        context = {
            'expenses': Expenses.objects.filter(category__in=ExpensesCategory.objects.filter(user_id=request.user.id))
        }
        return render(request, self.template_name, context)
