from django.urls import path,re_path
from FRG import views

urlpatterns=[
    re_path(r'^insert-store',views.storeInsert),
    re_path(r'^update-store',views.storeUpdate),
    re_path(r'^get-store',views.storeGet),
    re_path(r'^insert-mac',views.macInsert),
    re_path(r'^update-mac',views.macUpdate),
    re_path(r'^get-mac',views.macGet),
    re_path(r'^get-company',views.companyGet),

]