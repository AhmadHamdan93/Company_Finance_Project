
from sqlite3 import Date
from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30, verbose_name='Project Name',null=False, default='Project Default')
    period = models.IntegerField(verbose_name='Period',null=False,default=0)
    total_budget = models.IntegerField(verbose_name='Total Budget',null=False,default=0)
    description = models.TextField(verbose_name='Description',null=False,default='some info about project')
    image = models.ImageField(verbose_name='Image',null=False,default='FianceProject/project2.jpg')
    

    def __str__(self):
        return self.project_name


class yearBudget(models.Model):
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='Project',null=False)
    year = models.IntegerField(verbose_name='Year',null=False,default=2000)
    budget = models.IntegerField(verbose_name='Year Budget',null=False,default=0)

    def __str__(self):
        return str(self.project_id) + ' / ' + str(self.year)

class Expenses(models.Model):
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='Project',null=False)
    date = models.DateField(null=False,default=Date(2000,1,1))
    cost = models.IntegerField(null=False,default=0)
    operation = models.CharField(max_length=50,null=False,default='Operation Name')
    more_info = models.TextField(verbose_name='More Informations',null=False,default='some info about operation')

    def __str__(self):
        return str(self.project_id)  + ' / ' + self.operation


