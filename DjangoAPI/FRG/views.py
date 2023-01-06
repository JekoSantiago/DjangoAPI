from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse,HttpResponse,StreamingHttpResponse
from django.db import connection, connections, IntegrityError, DataError 
from DjangoAPI.helper import query_db
from datetime import date, datetime

@csrf_exempt
def storeInsert(request):
    kd_store = request.POST.get('kd_store')
    kd_regional = request.POST.get('kd_regional')
    nama_store = request.POST.get('nama_store')
    status = 'T'
    company = request.POST.get('company') or 'SM'
    gcashshop_id = request.POST.get('gcashshop_id') 

    res = query_db('frg','SELECT Company_MID FROM sm_company WHERE CompanyCode = \'' +str(kd_regional)+'\'')
    for item in res:
        for key,value in item.items():
            gcashmid_id = value

    try:
        data = query_db('frg','INSERT INTO ets.amu_stores_tab("kd_store","kd_regional","nama_store","status","company","gcashshop_id","gcashmid_id") VALUES( \''+str(kd_store)+'\',\''+str(kd_regional)+'\',\''+str(nama_store)+'\',\''+str(status)+'\',\''+str(company)+'\',\''+str(gcashshop_id)+'\',\''+str(gcashmid_id)+'\' ) RETURNING 1 AS RETURN, \'Succefully Added store\' AS MESSAGE')
        return JsonResponse(data,safe=False)
    except IntegrityError as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)
    except DataError  as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)

@csrf_exempt
def storeGet(request):
    kd_regional = request.POST.get('kd_regional') or 0
    try:
        if kd_regional == 0:
            data = query_db('frg','SELECT x.kd_store,x.kd_regional,x.nama_store,x.status,x.company,x.gcashshop_id,x.gcashmid_id,sc.company_id FROM ets.amu_stores_tab x INNER JOIN sm_company sc ON sc.CompanyCode = x.kd_regional WHERE status = \'T\'')
        else :
            data = query_db('frg','SELECT x.kd_store,x.kd_regional,x.nama_store,x.status,x.company,x.gcashshop_id,x.gcashmid_id,sc.company_id FROM ets.amu_stores_tab x INNER JOIN sm_company sc ON sc.CompanyCode = x.kd_regional WHERE kd_regional = \''+kd_regional+'\' AND status = \'T\'')
        return JsonResponse(data,safe=False)
    except:
        data = [{ "return" : -1, "message" : "Database Error, report to admin" }]
        return JsonResponse(data,safe=False)

@csrf_exempt
def storeUpdate(request):
    kd_store = request.POST.get('kd_store')
    kd_regional = request.POST.get('kd_regional')
    nama_store = request.POST.get('nama_store')
    status = request.POST.get('status') or 'T'
    gcashshop_id = request.POST.get('gcashshop_id') 

    try:
        data = query_db('frg','UPDATE ets.amu_stores_tab SET "kd_regional" =\''+ str(kd_regional)+'\', "nama_store" =\''+ str(nama_store)+'\', "status" =\''+ str(status)+'\', "gcashshop_id" =\''+ str(gcashshop_id)+'\' WHERE "kd_store" =\'' +str(kd_store)+'\' RETURNING 2 AS RETURN, \'Succefully Updated Store\' AS MESSAGE')
        return JsonResponse(data,safe=False)
    except IntegrityError as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)
    except DataError  as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)


@csrf_exempt
def macInsert(request):
    kd_store = request.POST.get('kd_store')
    jns_comp = request.POST.get('jns_comp')
    mac_address = request.POST.get('mac_address')
    aktif = 'T'
    tgl_buat = request.POST.get('tgl_buat') or datetime.today()
    tgl_ubah = request.POST.get('tgl_ubah') or datetime.today()
    user_id = request.POST.get('user_id') or 1
    company = request.POST.get('company') or 'SM'

    try:
        data = query_db('frg','INSERT INTO ets.amu_stores_mac_tab("kd_store","jns_comp","mac_address","aktif","tgl_buat","tgl_ubah","user_id","company") VALUES( \''+str(kd_store)+'\',\''+jns_comp+'\',\''+mac_address+'\',\''+aktif+'\',\''+str(tgl_buat)+'\',\''+str(tgl_ubah)+'\',\''+str(user_id)+'\',\''+company+'\' ) RETURNING 1 AS RETURN, \'Succefully Added Mac Store\' AS MESSAGE')
        return JsonResponse(data,safe=False)
    except IntegrityError as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)
    except DataError  as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)

@csrf_exempt
def macGet(request):
    kd_store = request.POST.get('kd_store') or 0
    
    # try:
    if kd_store == 0:
        data = query_db('frg','SELECT mt.kd_store,mt.jns_comp,mt.mac_address,mt.aktif,TO_CHAR(mt.tgl_buat:: DATE, \'Mon dd, yyyy\') as tgl_buat,TO_CHAR(mt.tgl_ubah:: DATE, \'Mon dd, yyyy\') as tgl_ubah,mt.user_id,mt.company, st.kd_regional FROM ets.amu_stores_mac_tab mt INNER JOIN ets.amu_stores_tab st ON mt.kd_store = st.kd_store WHERE mt.aktif = \'T\'')
    else:
        data = query_db('frg','SELECT "kd_store","jns_comp","mac_address","aktif",TO_CHAR(tgl_buat:: DATE, \'Mon dd, yyyy\') as tgl_buat,TO_CHAR(tgl_ubah:: DATE, \'Mon dd, yyyy\') as tgl_ubah,"user_id","company" FROM ets.amu_stores_mac_tab WHERE "aktif" = \'T\' AND "kd_store" = \''+kd_store+'\'')
    return JsonResponse(data,safe=False)
    # except:
    #     data = { "return" : -1, "message" : "Database Error, report to admin" }
    #     return JsonResponse(data,safe=False)

@csrf_exempt
def macUpdate(request):
    kd_store = request.POST.get('kd_store')
    jns_comp = request.POST.get('jns_comp')
    mac_address = request.POST.get('mac_address')
    aktif = request.POST.get('aktif') or 'T'
    tgl_ubah = request.POST.get('tgl_ubah') or datetime.today()
    user_id = request.POST.get('user_id') or 1

    try:
        data = query_db('frg','UPDATE ets.amu_stores_mac_tab SET "jns_comp" =\''+ str(jns_comp)+'\', "mac_address" =\''+ str(mac_address)+'\', "aktif" =\''+ str(aktif)+'\',  "tgl_ubah" =\''+ str(tgl_ubah)+'\', "user_id" =\''+ str(user_id)+'\' WHERE "kd_store" =\'' +str(kd_store)+'\' RETURNING 2 AS RETURN, \'Succefully Updated Mac Store\' AS MESSAGE')
        return JsonResponse(data,safe=False)
    except IntegrityError as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)
    except DataError  as e:
        data = [{"return" : -1, "message" : str(e)}]
        return JsonResponse(data,safe=False)

@csrf_exempt
def companyGet(request):
    try:
        data = query_db('frg','SELECT "Company_ID", "CompanyCode", "Company_MID", "Company" FROM sm_company')
        return JsonResponse(data,safe=False)
    except:
        data = { "return" : -1, "message" : "Database Error, report to admin" }
        return JsonResponse(data,safe=False)

