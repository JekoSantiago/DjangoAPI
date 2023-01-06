from django.urls import path,re_path
from Galaxy import views

urlpatterns=[
    re_path(r'^get-operator',views.operatorGet),
    re_path(r'^insert-operator',views.operatorInsert),
    re_path(r'^update-operator',views.operatorUpdate),
    re_path(r'^extract',views.export_page),
    re_path(r'^viewxls',views.viewxls),



]