from django.contrib import admin
from api.models import *

# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass
@admin.register(UserIssue)
class UserIssue(admin.ModelAdmin):
    pass

