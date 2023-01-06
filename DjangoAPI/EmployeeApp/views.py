from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse,HttpResponse
from django.db import connection

@csrf_exempt
def departmentGet(request):
    deptID = request.POST.get('id') or 0
    with connection.cursor() as cursor:
        cursor.execute("EXEC sp_Department_Get " + str(deptID))
        data = cursor.fetchall()
    return JsonResponse(data,safe=False)

@csrf_exempt
def departmentInsert(request):
    deptName = request.POST.get('deptName')
    with connection.cursor() as cursor:
        cursor.execute("EXEC sp_Department_Insert '" + str(deptName) + "'")
        data = cursor.fetchall()
    return JsonResponse(data,safe=False)
