from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,yearBudget,Expenses


# Create your views here.

def all_projects(request):
    projects = Project.objects.all()
    return render(request,'FinanceProject/ProjectListPage.html',{'projects':projects})


def project_detail(request,id):
    project = serializers.serialize("json", Project.objects.filter(id=id))
    budget = serializers.serialize("json", yearBudget.objects.filter(project_id=id))
    expenses = serializers.serialize("json", Expenses.objects.filter(project_id=id))
    context = {'project':project,'budget':budget,'expenses':expenses,'currentID':id}
    return render(request,'FinanceProject/ProjectDetailsPage.html',context)


def budget(request,id):
    project = serializers.serialize("json", Project.objects.filter(id=id))
    budget = serializers.serialize("json", yearBudget.objects.filter(project_id=id).order_by('-id'))
    context = {'project':project,'budget':budget,'currentID':id}
    return render(request,'FinanceProject/budget.html',context)


def expenses(request,id):
    project = serializers.serialize("json", Project.objects.filter(id=id))
    expense = serializers.serialize("json", Expenses.objects.filter(project_id=id).order_by('-id'))
    budget = serializers.serialize("json", yearBudget.objects.filter(project_id=id).order_by('-id'))
    context = {'project':project,'expense':expense,'budget':budget,'currentID':id}
    return render(request,'FinanceProject/expenses.html',context)


# ---------------------------------------------------
# ---------------------------------------------------
# ------------------ API funtions -------------------
# ---------------------------------------------------
# ---------------------------------------------------
#
# ---------------------------------------------------
# ---------------------------------------------------
# -------------- start budget functions -------------
# ---------------------------------------------------
# ---------------------------------------------------
# update budget value  
def updateBudget(request):
    if request.method == 'POST':
        # get data from request   /// projectID
        projectID = request.POST.get('projectID')
        currentID = request.POST.get('currentID')
        yearVal = request.POST.get('year')
        budgetVal = request.POST.get('budget')
        # --------------------------------
        # --------------------------------
        currentProject = yearBudget.objects.get(id=currentID)
        currentProject.year = yearVal
        currentProject.budget = budgetVal
        currentProject.save()
        # return all budget
        allBudget = serializers.serialize("json", yearBudget.objects.filter(project_id=projectID).order_by('-id'))
        return HttpResponse(allBudget, content_type="application/json")  # , content_type="application/json"

# insert budget   
def insertBudget(request):
    if request.method == 'POST':
        # get data from request
        currentProjectID = request.POST.get('projectID')
        yearVal = request.POST.get('year')
        budgetVal = request.POST.get('budget')
        # select object from database where its same project_id for
        # for insert new object in budget table
        currentProject = Project.objects.get(id=currentProjectID)
        # create new budget object with fake data for get id 
        newBudget = yearBudget(project_id=currentProject,year=yearVal,budget=budgetVal)
        newBudget.save()
        return HttpResponse()

# delete budget value  
def deleteBudget(request):
    if request.method == 'POST':
        # get data from request
        projectID = request.POST.get('projectID')
        currentID = request.POST.get('currentID')
        currentProject = yearBudget.objects.get(id=currentID)
        currentProject.delete()
        # return all budget
        allBudget = serializers.serialize("json", yearBudget.objects.filter(project_id=projectID).order_by('-id'))
        return HttpResponse(allBudget, content_type="application/json")  # , content_type="application/json"

# ---------------------------------------------------
# ---------------------------------------------------
# -------------- end budget functions ---------------
# ---------------------------------------------------
# ---------------------------------------------------

# ---------------------------------------------------
# ---------------------------------------------------
# -------------- start expenses functions -----------
# ---------------------------------------------------
# ---------------------------------------------------
# update expenses value  
def updateExpenses(request):
    if request.method == 'POST':
        # get data from request
        projectID = request.POST.get('projectID')
        currentID = request.POST.get('currentID')
        dateVal = request.POST.get('date')
        costVal = request.POST.get('cost')
        operationVal = request.POST.get('operation')
        moreInfoVal = request.POST.get('moreInfo')
        # --------------------------------
        # --------------------------------
        currentExpense = Expenses.objects.get(id=currentID)
        currentExpense.date = dateVal;
        currentExpense.cost = costVal;
        currentExpense.operation = operationVal;
        currentExpense.more_info = moreInfoVal;
        currentExpense.save()
        # return all Expenses
        allExpenses = serializers.serialize("json", Expenses.objects.filter(project_id=projectID).order_by('-id'))
        return HttpResponse(allExpenses, content_type="application/json")

# insert expenses   
def insertExpenses(request):
    if request.method == 'POST':
        currentProjectID = request.POST.get('projectID')
        dateVal = request.POST.get('date')
        costVal = request.POST.get('cost')
        operationVal = request.POST.get('operation')
        moreInfoVal = request.POST.get('moreInfo')
        # select object from database where its same project_id for
        # for insert new object in expense table
        currentProject = Project.objects.get(id=currentProjectID)
        # create new expense object with fake data for get id 
        newExpense = Expenses(project_id=currentProject)
        newExpense.date = dateVal;
        newExpense.cost = costVal;
        newExpense.operation = operationVal;
        newExpense.more_info = moreInfoVal;
        newExpense.save()
    
        return HttpResponse()

# delete expenses value  
def deleteExpenses(request):
    if request.method == 'POST':
        # get data from request
        projectID = request.POST.get('projectID')
        currentID = request.POST.get('currentID')
        currentProject = Expenses.objects.get(id=currentID)
        currentProject.delete()
        # return all Expenses
        allExpenses = serializers.serialize("json", Expenses.objects.filter(project_id=projectID).order_by('-id'))
        return HttpResponse(allExpenses, content_type="application/json")
# ---------------------------------------------------
# ---------------------------------------------------
# -------------- end expenses functions -------------
# ---------------------------------------------------
# ---------------------------------------------------
