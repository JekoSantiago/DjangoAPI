from django.urls import path,re_path
from EmployeeApp import views

urlpatterns=[
    re_path(r'^get-dept',views.departmentGet),
    re_path(r'^insert-dept',views.departmentInsert),

]