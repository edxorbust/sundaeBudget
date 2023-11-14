from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logout_view, name="logout"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('add_expense', views.add_expense, name="add_expense"),
    path('budget', views.budget, name="budget"),
    path('add_budget', views.add_budget, name="add_budget"),
    path('expense_history', views.expense_history, name="expense_history"),
    path('edit_budget/<int:id>', views.edit_budget, name="edit_budget"),
    path('delete_expense/<int:id>', views.delete_expense, name="delete_expense")

]