from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import date
from django.core.paginator import Paginator
from django.db.models import Sum
from .models import User, Category, Expense, Budget
# Create your views here.

def add_budget(request):
    if request.method == "POST":
        amount = request.POST["amount"]
        user = request.user
        category = request.POST["category"]
        nCategory = Category.objects.get(name=category)
        nBudget = Budget(
            amount = amount,
            user = user,
            category = nCategory
        )
        nBudget.save()
        return HttpResponseRedirect(reverse("budget"))
    else:
        categories = Category.objects.all()
        taken_categories = Budget.objects.filter(user=request.user).values_list('category__name', flat=True)
        available_categories = [category.name for category in categories if category.name not in taken_categories]
        return render(request, "budget/addBudget.html", {
                "categories":available_categories
            })
    

def budget(request):
    budgetList = Budget.objects.filter(user=request.user)
    cat_number = Category.objects.all().count()
    if budgetList.count() == cat_number:
        addButton = False
    else:
        addButton = True
    budgetSum = 0.00
    for budget in budgetList:
        budgetSum += budget.amount
    return render(request, "budget/budget.html", {
        "budgetSum":budgetSum,
        "budgets":budgetList,
        "addButton":addButton
    })


def edit_budget(request, id):
    if request.method == "POST":
        nBudget = Budget.objects.get(id=id)
        nBudget.amount = request.POST['amount']
        nBudget.save()
        return HttpResponseRedirect(reverse("budget"))
    else:
        budget = Budget.objects.get(id=id)
        return render(request, "budget/editBudget.html", {
            "budget":budget
        })
    

def add_expense(request):
    if request.method == "POST":
        amount = request.POST["amount"]
        user = request.user
        category = request.POST["category"]
        nCategory = Category.objects.get(name=category)
        type = request.POST["type"]
        if 'essential' in request.POST:
            essential = True
        else:
            essential = False
        if 'recurrent' in request.POST:
            recurrent = True
            frecuency = request.POST["frecuency"]
        else:
            recurrent = False
            frecuency = 'no'

        nExpense = Expense(
            amount = amount,
            user = user,
            category = nCategory,
            type = type,
            essential = essential,
            recurrent = recurrent,
            frecuency = frecuency
        )
        nExpense.save()


        return HttpResponseRedirect(reverse("index"))
    else:
        categories = Category.objects.all()
        return render(request, "budget/addExpense.html", {
                "categories":categories
            })


def index(request):
    if request.method == "POST":
        currentUser = request.user
        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        budgetList = Budget.objects.filter(user=currentUser)
        budgetSum = 0.00
        for budget in budgetList:
            budgetSum += budget.amount
        expenseList = Expense.objects.filter(date__month=currentMonth, date__year=currentYear, user=currentUser) 
        expenseSum = 0.00
        for expense in expenseList:
            expenseSum += expense.amount
        remainingBudget = budgetSum - expenseSum
        expenseCatSums = Expense.objects.filter(date__month=currentMonth, date__year=currentYear, user=currentUser).values('category', 'category__name').annotate(total_amount=Sum('amount'))
        return render(request, "budget/index.html", {
            "expenseSum":round(expenseSum,2),
            "expenseList":expenseList,
            "remainingBudget":round(remainingBudget, 2),
            "budgetList":budgetList,
            "budgetSum":budgetSum,
            "expenseCatSums":expenseCatSums
        })
    else:
        if request.user.is_authenticated:
            currentUser = request.user
            currentMonth = date.today().month
            currentYear = date.today().year
            budgetList = Budget.objects.filter(user=currentUser)
            budgetSum = 0.00
            for budget in budgetList:
                budgetSum += budget.amount
            expenseList = Expense.objects.filter(date__month=currentMonth, date__year=currentYear, user=currentUser) 
            expenseSum = 0.00
            for expense in expenseList:
                expenseSum += expense.amount
            remainingBudget = budgetSum - expenseSum
            expenseCatSums = Expense.objects.filter(date__month=currentMonth, date__year=currentYear, user=currentUser).values('category', 'category__name').annotate(total_amount=Sum('amount'))
            overBudgetCat = []
            for cat in expenseCatSums:
                for bud in budgetList:
                    if bud.category.name == cat["category__name"]:
                        total = bud.amount - cat["total_amount"]
                        if total < 0:
                            overBudgetCat.append(bud.category.name)
            return render(request, "budget/index.html", {
                "expenseSum":round(expenseSum,2),
                "expenseList":expenseList,
                "remainingBudget":round(remainingBudget, 2),
                "budgetList":budgetList,
                "budgetSum":budgetSum,
                "expenseCatSums":expenseCatSums,
                "overBudgetCat":overBudgetCat
            })
        else:
            return HttpResponseRedirect(reverse('login'))


def expense_history(request):
    if request.method == "POST":
        act_date = request.POST["month"]
        expensesList = Expense.objects.filter(date__month=act_date, user=request.user).order_by('-date')
        paginator = Paginator(expensesList, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "budget/expenseHistory.html", {
            "expensesList":page_obj,
            "act_month":act_date
        })
    else:
        act_date = date.today()
        expensesList = Expense.objects.filter(date__month=act_date.month, user=request.user).order_by('-date')
        paginator = Paginator(expensesList, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "budget/expenseHistory.html", {
            "expensesList":page_obj,
            "act_month":act_date.month
        })

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return HttpResponseRedirect(reverse('expense_history'))
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "budget/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "budget/login.html")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "budget/register.html", {
                "message": "Passwords must match."
            })
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "budget/register.html", {
                "message": "Username already taken."
            })
        login(request, user)

        

        return HttpResponseRedirect(reverse("add_budget"))
    else:
        return render(request, "budget/register.html")