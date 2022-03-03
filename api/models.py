from django.db import models
import datetime


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    


class Project(models.Model):
    project_id  = models.CharField(max_length=20,null=False, blank=False,unique=True)
    name =  models.CharField(max_length=1500, blank=True, null=True)
    date = models.DateField(default= datetime.datetime.now )
    # username = models.CharField(max_length=255)



class Issue(models.Model):
    issue  = models.ForeignKey(Project,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1500, blank=True, null=True)
    assignee = models.CharField(max_length=1500, blank=True, null=True)
    sprint = models.CharField(max_length=1500, blank=True, null=True)
    type  = models.CharField(max_length=1500, blank=True, null=True)
    status = models.CharField(max_length=1500, blank=True, null=True)
    date_created = models.DateField(default= datetime.datetime.now )

class UserIssue(models.Model):
    user_rel = models.ForeignKey(Users,on_delete=models.PROTECT)
    issue_rel = models.ForeignKey(Issue,on_delete=models.CASCADE)
    date_assigned= models.DateField(default= datetime.datetime.now )

class Labels(models.Model):
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name='labels')
    label = models.CharField(max_length=1500, blank=True, null=True)