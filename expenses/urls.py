from django.urls import path
from .views import ExpensesCategoryView,ExpensesAddView,ExpensesView
urlpatterns = [
    path('category/', ExpensesCategoryView.as_view(), name='expenses_category'),
    path('create/', ExpensesAddView.as_view(), name='expenses_create'),
    path('', ExpensesView.as_view(), name='expenses'),
]