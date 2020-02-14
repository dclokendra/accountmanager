from .models import ExpensesCategory, Expenses
from django import forms


class ExpensesCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Category Title'}))

    class Meta:
        model = ExpensesCategory
        fields = ['title',]


class ExpensesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=ExpensesCategory.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Expenses
        fields = '__all__'
