from django.db import models


# class Users(models.Model):
#     username = models.CharField(max_length=255, primary_key=True)

class Project(models.Model):
    project_id  = models.CharField(max_length=20,null=False, blank=False,unique=True)
    name =  models.CharField(max_length=1500, blank=True, null=True)
    # username = models.CharField(max_length=255)



class Issue(models.Model):
    issue_id  = models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=1500, blank=True, null=True)
    label = models.CharField(max_length=1500, blank=True, null=True)
    assignee = models.CharField(max_length=1500, blank=True, null=True)
    sprint = models.CharField(max_length=1500, blank=True, null=True)
    type  = models.CharField(max_length=1500, blank=True, null=True)
    status = models.CharField(max_length=1500, blank=True, null=True)