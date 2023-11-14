from django.contrib import admin
from .models import Category, User, Expense, Budget
# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Budget)
