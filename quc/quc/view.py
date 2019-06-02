# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
def Welcome(request):
    context = {}
    context["des"] = "中国秦川联盟|中国秦川科技联盟|中国秦川学术联盟\
|天狼队|中国米兔联盟|www.quc.com"
    context["tenet"] = "大鹏一日同风起，扶摇直上九万里。\
假令风歇时下来，犹能簸却沧溟水。"
    context["title"] = "中国秦川联盟"
    context['Welcome'] = '欢迎来到中国秦川联盟'
    context["admin"] = "管理员"
    #context["file1"] = ""
    context["show"] = "公告"
    context["location"] = "地图"
    
    return render(request, 'Welcome.html', context)

def admin(request):
    context = {}
    context["des"] = "管理员通道|www.qinchuanunion.tk"
    context["tenet"] = "大鹏一日同风起，扶摇直上九万里。\
假令风歇时下来，犹能簸却沧溟水。"
    context["title"] = "管理员通道"
    context["Welcome"] = "管理员专用通道"
    
    return render(request, 'admin.html', context)

def show(request):
    context = {}
    context["show"] = "公告"
    return render(request, 'show.html', context)

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse("ip: "+ip+"\n"+"你已经被我们监控")

def upload(request):
    if request.method == 'POST':
        obj = request.FILES.get('fafafa')
        import os
        print obj.name
        f = open(os.path.join(BASE_DIR, 'static', 'pic', obj.name), 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        return  HttpResponse('OK')
    return render(request, 'upload.html')

def notfound(request):
    context = {}
    context['path'] = request.path
    return render(request, '404.html', context)

