from django.urls import path
from . import views

urlpatterns =[
    path('',views.all_projects,name="allprojects"),
    path('projectdetails/<int:id>/',views.project_detail,name="projectdetails"),
    path('budget/<int:id>/',views.budget,name="budget"),
    path('expenses/<int:id>/',views.expenses,name="expenses"),
    # for budget function
    path('pathinsertBudget/',views.insertBudget,name="insertBudget"),
    path('pathdeleteBudget/',views.deleteBudget,name="deleteBudget"),
    path('pathupdateBudget/',views.updateBudget,name="updateBudget"),
    # for expenses function
    path('pathinsertExpenses/',views.insertExpenses,name="insertExpenses"),
    path('pathupdateExpenses/',views.updateExpenses,name="updateExpenses"),
    path('pathdeleteExpenses/',views.deleteExpenses,name="deleteExpenses"),
]