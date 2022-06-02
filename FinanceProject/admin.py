import imp
from django.contrib import admin
from .models import Project,yearBudget, Expenses
# Register your models here.

admin.site.register(Project)
admin.site.register(Expenses)
admin.site.register(yearBudget)