from django.shortcuts import render
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from api.models import *
import random
import json
import string

def index(request):
    return HttpResponse(json.dumps({"status": "200","message":"HI"}), content_type='application/json')


def create_project(request):
    NAME = request.POST.get('name')
    id_rand  = ''.join(random.choices(
                    string.ascii_letters + string.digits, k=10))
    try:
        Project(project_id=id_rand, name = NAME).save()
        return HttpResponse(json.dumps({"status": "200","project_id":id_rand}), content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')

def create_issue(request):
    try:
        obj = Project.objects.get(project_id=request.POST.get('project_id'))
        a = Issue(issue = obj, title=request.POST.get('title'),assignee=request.POST.get('assignee'),type=request.POST.get('type'),sprint=request.POST.get('sprint'),status=request.POST.get('status'))
        a.save()
        Labels(issue=a,label=request.POST.get('labels')).save()
        return HttpResponse(json.dumps({"status": "200","Issue":"created","IssueId":a.id}), content_type='application/json')

    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')
    
def get_all_projects(request):
    d = []
    for i in Project.objects.all():
            d.append({"projectId": i.project_id,
                      "projectName": i.name,"Date":i.date.strftime("%m/%d/%Y, %H:%M:%S")})
    return HttpResponse(json.dumps({"Projects": d}), content_type='application/json')

def get_project_details(request):
    project_id = request.POST.get('project_id')
    obj = Project.objects.get(project_id=project_id)
    issues = []
    for i in Issue.objects.filter(issue=obj).all():
        labels = []
        for j in Labels.objects.filter(issue=i).all():
            labels.append(j.label)
        issues.append({"Issue Id":i.id,"Title":i.title,"Labels":labels,"Type":i.type,"Sprint":i.sprint,"Status":i.status,"Assignee":i.assignee,"Date Created":i.date_created.strftime("%m/%d/%Y, %H:%M:%S")})
    
    return HttpResponse(json.dumps({"status":"200","projectId":project_id,"projectName":obj.name,"Issues":issues}), content_type='application/json')

def get_all_issue_of_project(request):
    project_id = request.POST.get('project_id')
    limit = request.POST.get('limit')
    offset = request.POST.get('offset')
    obj = Project.objects.get(project_id=project_id)
    issues = []
    for i in Paginator(Issue.objects.filter(issue=obj).all(), limit).page(offset):
        labels = []
        for j in Labels.objects.filter(issue=i).all():
            labels.append(j.label)
        issues.append({"Issue Id":i.id,"Title":i.title,"Labels":labels,"Type":i.type,"Sprint":i.sprint,"Status":i.status,"Assignee":i.assignee,"Date Created":i.date_created.strftime("%m/%d/%Y, %H:%M:%S")})
    
    return HttpResponse(json.dumps({"status":"200","Issues":issues}), content_type='application/json')

def assign_issue(request):
    issue_id = request.POST.get('issue_id')
    user_id = request.POST.get('user_id')
    try:
        UserIssue(user_rel=Users.objects.get(user_id=user_id),issue_rel=Issue.objects.get(id=issue_id)).save()
        return HttpResponse(json.dumps({"status":"200","message":f"Issue successfully assigned to {Users.objects.get(user_id=user_id).username}"}), content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')

def get_issue_assigned_to_user(request):
    user_id = request.POST.get('user_id')
    issues = []
    try:
        for i in UserIssue.objects.filter(user_rel=Users.objects.get(user_id=user_id)).all().order_by("-date_assigned"):
            issues.append({"Issue Id":i.id,"Date Created":i.date_assigned.strftime("%m/%d/%Y, %H:%M:%S")})
        return HttpResponse(json.dumps({"userId":user_id,"issues":issues}), content_type='application/json')
    except:
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')

def add_label_to_issue(request):
    issue_id = request.POST.get('issue_id')
    label = request.POST.get('label')
    try:
        Labels(issue=Issue.objects.get(id=issue_id), label=label).save()
        return HttpResponse(json.dumps({"status":"200","message":"Label added successfully"}), content_type='application/json')
    except:
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')

def search_issues(request):
    search_param = request.POST.get('search_param')
    results = []
    try:
        for i in Project.objects.filter(name__icontains=search_param).all():
            results.append({"projectName":i.name,"projectId":i.id})

        for i in Issue.objects.filter(title__icontains=search_param).all():
            results.append({"issueTitle":i.title,"issueId":i.id})

        for i in Issue.objects.filter(assignee__icontains=search_param).all():
            results.append({"issueAssignee":i.assignee,"issueId":i.id})

        for i in Issue.objects.filter(sprint__icontains=search_param).all():
            results.append({"issueSprint":i.sprint,"issueId":i.id})
    
        for i in Issue.objects.filter(type__icontains=search_param).all():
            results.append({"issueType":i.type,"issueId":i.id})


        for i in Issue.objects.filter(status__icontains=search_param).all():
            results.append({"issueStatus":i.status,"issueId":i.id})
        
        for i in Labels.objects.filter(label__icontains=search_param).all():
            results.append({"issueLabel":i.label,"issueId":i.issue.id})
  
    
        return HttpResponse(json.dumps({"status":"200","result":results}), content_type='application/json')
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')