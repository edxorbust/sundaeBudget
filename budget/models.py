from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=140)
    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.FloatField(default=0)
    user = models.ForeignKey(User, related_name=("author"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name=("category"), on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    essential = models.BooleanField(default=False)
    recurrent = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    frecuency = models.CharField(max_length=140)



class Budget(models.Model):
    amount = models.FloatField(default=0)
    user = models.ForeignKey(User, related_name=("userBudget"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name=("categoryBudget"), on_delete=models.CASCADE)
