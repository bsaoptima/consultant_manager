from django.db import models
from django.urls import reverse

# Create your models here.

class Consultant(models.Model):
    
    ''' 
    Consultant Class 
    -Who they are
    -The team they are in (figure out the foreign keys)
    
    Connections:
    -Department() : One to Many
    -Team() : One to Many
    '''
    
    #Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    department_name = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    team_name = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, default="Unassigned")

    #Metadata
    class Meta:
        ordering = ['last_name', 'first_name']
    
    #Methods
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        '''String for Representing the Model Object.'''
        return f'{self.last_name}, {self.first_name}'
    

class Department(models.Model):
    
    '''
    Department Class
    -Can be used to describe the area where a consultant works
    
    Connections:
    -Consultant() : One to One in this direction
    '''
    
    #Fields
    department_name = models.CharField(max_length=100)
    
    #Methods
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        '''String for Representing the Model Object.'''
        return self.department_name
    

class Team(models.Model):
    
    '''
    In which team is the consultant working
    
    FIGURE OUT THE FOREIGN KEYS
    
    Connections:
    -Consultant() : One to One in this direction
    '''
    
    #Fields
    team_name = models.CharField(max_length=100)
    team_project = models.OneToOneField('Project', on_delete=models.SET_NULL, null=True)
    
    
    #Methods
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.team_name


class Project(models.Model):
    
    #Fields
    project_name = models.CharField(max_length=100)
    project_client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    project_description = models.TextField(max_length=200)
    project_startDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    project_endDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.project_name


class Client(models.Model):
    
    #Fields
    client_name = models.CharField(max_length=100) 
    client_primary_contact = models.CharField(max_length=100)
    client_number_of_projects = models.IntegerField() #how many projects have we completed with this client
    
    def __str__(self):
        return self.client_name