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
        Issue(issue_id = obj, title=request.POST.get('title'),label=request.POST.get('labels'),assignee=request.POST.get('assignee'),type=request.POST.get('type'),sprint=request.POST.get('sprint'),status=request.POST.get('status')).save()
        return HttpResponse(json.dumps({"status": "200","Issue":"created"}), content_type='application/json')

    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"status": "500"}), content_type='application/json')
    
def get_all_projects(request):
    d = []
    for i in Project.objects.all():
            d.append({"projectId": i.project_id,
                      "projectName": i.name})
    return HttpResponse(json.dumps({"Projects": d}), content_type='application/json')

def get_project_details(request):
    project_id = request.POST.get('project_id')
    obj = Project.objects.get(project_id=project_id)
    issues = []
    for i in Issue.objects.filter(issue_id=obj).all():
        issues.append({"Title":i.title,"Label":i.label,"Type":i.type,"Sprint":i.sprint,"Status":i.status})
    
    return HttpResponse(json.dumps({"status":"200","projectId":project_id,"projectName":obj.name,"Issues":issues}), content_type='application/json')

def get_all_issue_of_project(request):
    project_id = request.POST.get('project_id')
    limit = request.POST.get('limit')
    offset = request.POST.get('offset')
    obj = Project.objects.get(project_id=project_id)
    issues = []
    for i in Paginator(Issue.objects.filter(issue_id=obj).all(), limit).page(offset):
        issues.append({"Title":i.title,"Label":i.label,"Type":i.type,"Sprint":i.sprint,"Status":i.status})
    
    return HttpResponse(json.dumps({"status":"200","Issues":issues}), content_type='application/json')
