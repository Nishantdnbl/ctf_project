

from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from Flags.models import User, Submit_flag, flg4
import json


def index(request):
    return render(request, "web/index.html")

def login(request):
    nam = request.POST.get('name')
    id = int(request.POST.get('id'))
    
    existing_user = User.objects.filter(name_id=id).first()
    
    if existing_user:
        
        existing_user.name = nam
        existing_user.save()
    else: 
        
        new_user = User(
            name_id=id,
            name=nam,
            flag1=0,
            flag2=0,
            flag3=0,
            flag4=0,
            flag5=0
        )
        new_user.save()

    data = {"name": nam, "id": id}
    return render(request, "web/dashboard.html", data)
def submit(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    msg = "submit the flag here"
    if request.method == 'POST':
        flg = request.POST.get("User_inp")
        print(flg)
        
        if flg:
            print(flg)
            user = User.objects.get(name_id=id)
            real_flag = Submit_flag.objects.first()
            if flg == real_flag.flag_1:
                user.flag1 = 1
                msg = "Flag1 submited"
                user.save()
            elif flg == real_flag.flag_2:
                user.flag2 = 1
                msg = "Flag2 submited"
                user.save()
            elif flg == real_flag.flag_3:
                user.flag3 = 1
                msg = "Flag3 submited"
                user.save()
            elif flg == real_flag.flag_4:
                user.flag4 = 1
                msg = "Flag4 submited"
                user.save()
            elif flg == real_flag.flag_5:
                user.flag5 = 1
                msg = "Flag5 submited"
                user.save
            

    print(name, id)

    data = {"name": name, "id": id, "msg" : msg}

    return render(request, "web/submitFLG.html", data)

def flg3(request):
    if request.method == 'POST':
        return HttpResponse("Tu_Tu_Tu_Tutu_Tar_…._Orr_Ja_Raha_Hai_Tiger_On_Mission_Dobarah")
    else:
        return HttpResponseRedirect("/")
    
def flag4(request):# select * from Flags_flg4

    flag_value = None

    if request.method == 'POST':
       
        data = json.loads(request.body.decode('utf-8'))
        post = data.get('query', '')
        post = f"select {post} from Flags_flg4"
        flag_valu =  flg4.objects.raw(post)
        for flg in flag_valu:
            print(flg)
        
        return HttpResponse(flg)
    else:
        return HttpResponseRedirect("/")

        
def challange_1(request):
    name_ = request.POST.get("name")
    id = request.POST.get("id")
    print(name_)
    data = {"name": name_, "flg": "flg1", "id" : id}
    return render(request, "web/flag1.html", data)


def challange_2(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    print(name)
    flag2 = "Flag2:all_is_well"
    data = {"name" : name, "flg" : flag2, "id" : id}
    return render(request, "web/flag2.html", data)

def challange_3(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    print(name)
    data = {"name" : name, "id" : id}
    return render(request, "web/flag3.html", data)
    
def challange_4(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    print(name)
    data = {"name" : name, "id" : id}
    return render(request, "web/flag4.html", data)
    
def challange_5(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    print(name)
    data = {"name" : name, "id" : id}
    return render(request, "web/flag5.html", data)
    

