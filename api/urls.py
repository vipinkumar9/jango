from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),  
    path('createProject/', views.create_project, name='create_a_project'), 
    path('createIssue/', views.create_issue, name='create_a_issue'), 
    path('getAllProject/', views.get_all_projects, name='Get all project'), 
    path('getProjectDetails/', views.get_project_details, name='get_project_details'), 
    path('getAllIssueOfProject/', views.get_all_issue_of_project, name='get_all_issue_of_project'), 
    path('assignIssue/', views.assign_issue, name='assign_issue'), 
    path('getIssueAssignedToUser/', views.get_issue_assigned_to_user, name='get_issue_assigned_to_user'), 
    path('addLabel/', views.add_label_to_issue, name='add_label_to_issue'), 

]
