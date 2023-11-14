# Sundae's Budget Planner

Why Sundae? The name is in honor of my cat Sundae, she is a 1 year old tabby cat, she was always playing with me while I was coding and helping me relaxing with some difficult tasks.

# Distinctiveness and complexity

This app was made due to the need to be able to keep track of my monthly expenses with a system to add each expense deducted from a monthly budget attached to a specific category.

It was created using Django for the backend and Javascript for the frontend. In the application you can see a client-server architecture where the backend processes all the data requested by the client that is extracted from a database using SQLite with the functions acquired by default in the base Django template. The server is capable of storing amounts of expenses obtained through the client that the user provides according to a specific category, the type of expense such as cash or credit, whether this expense is recurring or non-recurring and whether the expense is essential or No, in order to have better control with expenses that are not essential or that will only be incurred once so that the user can take them into account and try to reduce or eliminate them completely.

When the client requests it, the server can extract data from the database according to the user who has logged in, the date (month and year) in which the request was made and a specific category, the data is processed subtracting the expenses from the budget established for that category and sending the client all the required data, including the sum of budgets, the sum of expenses, and the remaining monthly budget.

On the client side you can obtain all the expenses and budgets to be entered, requests are made to the server with the user's information and the specific date, there is no data processing on the part of the client. Javascript is used to enable and disable fields of a form, as well as to manage the animation of the navigation bar and also to create graphics that are based on the budget and expense data provided by the server according to the information of the user.

Unlike other types of applications such as social networks or marketplaces, this application is specialized in managing quantities, creating statistical data, processing numerical data in relation to limits established by a user, instead of information about people, images or articles. for sale, as a social network or marketplace would do respectively. It also has several class models to define each element used in each characteristic of the application, you can see the complexity of the project unlike the previous ones with the largest number of models and the largest number of interactions between them that would create an ecosystem. little more advanced than what was done in previous projects.

# Description of the project

With this app the user its able to create a monthly budget with categories and add all the expenses made through the month, the app will show how much the user has left to spend during the month according to the total budget, if the user spent more than the actual budget the app will alert the user with the total and also with the individual budget affected, if the user is almost completing a budget category with expenses the app will show an alert. The app will show a history of all the expenses made by the user with the option to be deleted.

# How to run the app

In order to run the app the server just needs to be started by using: 'python manage.py runserver' command inside the 'budgetapp' directory.

# Files

## urls.py

This file contains all the routes for all the templates created for every view inside this app.

## addBudget.html

This is the template used to show the interface when the user is adding a budget.

## addExpense.html

This is the template used to show the interface when the user is adding a expense that also will show on the expense history.

## budget.html

This is the template used to show the interface with all the budgets that the user has added.

## editBudget.html

This is the template used to show the interface for when the user needs to edit a specific budget.

## expenseHistory.html

This is the template to show all the expenses the user has added.

## index.html

This is the template to show the total of expenses the user has added by category and also will show the total budget of all categories that the user has.

## layout.html

This is the template to show the navigation bar, header, and all the interface items that doesn't change.

## login.html

This is the template to show the form used to access the user's account.

## register.html

This is the template used to show the form to create a new account.

## styles.css

This file contains all the classes used with all the html files.

## script.js

This file contains all the javascript functions used with the html files.