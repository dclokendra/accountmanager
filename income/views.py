from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from .forms import IncomeCategoryForm, IncomeForm
from .models import IncomeCategory, Income


class IncomeCategoryView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'income_category.html'

    def get(self, request):
        context = {
            'form': IncomeCategoryForm(),
            'category': IncomeCategory.objects.filter(user_id=request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = IncomeCategoryForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "Category added Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Category creation Failed")
            return redirect('income_category')


class IncomeAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'add_income.html'

    def get(self, request):
        context = {
            'form': IncomeForm(request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = IncomeForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Income Created Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Income creation Failed")
            return redirect('income_create')


class IncomeView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'income.html'

    def get(self, request):
        context = {
            'income': Income.objects.filter(category__in=IncomeCategory.objects.filter(user_id=request.user.id))
        }
        return render(request, self.template_name, context)


class IncomeEditView(UpdateView):
    template_name = 'edit_income.html'
    form = IncomeForm
    fields = ['title', 'price', 'description', 'image', 'category']
    success_url = reverse_lazy('income')

    def get_context_data(self, **kwargs):
        context = super(IncomeEditView, self).get_context_data()
        context['form'] = IncomeForm(self.request.user.id, instance=Income.objects.get(slug=self.kwargs['slug']))
        return context

    def get_object(self, queryset=None):
        queryset = Income.objects.filter(slug=self.kwargs['slug'])
        return super(IncomeEditView, self).get_object(queryset)


class IncomeDeleteView(DeleteView):
    template_name = 'income_confirm_delete.html'
    success_url = reverse_lazy('income')
    model = Income
    slug_field = 'slug'


class IncomeCategoryEditView(UpdateView):
    form_class = IncomeCategoryForm
    template_name = 'income_category_update.html'
    success_url = reverse_lazy('income_category')
    queryset = None

    def get_context_data(self, **kwargs):
        context = super(IncomeCategoryEditView, self).get_context_data()
        context['form']=IncomeCategoryForm(instance=IncomeCategory.objects.get(slug=self.kwargs['slug']))
        return context

    def get_object(self, queryset=None):
        queryset = IncomeCategory.objects.filter(slug=self.kwargs['slug'])
        return super(IncomeCategoryEditView,self).get_object(queryset)


class IncomeCategoryDeleteView(DeleteView):
    template_name = 'income_confirm_delete.html'
    success_url = reverse_lazy('income_category')
    model = IncomeCategory
    slug_field = 'slug'
