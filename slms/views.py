from django.shortcuts import render,redirect,HttpResponse
from slmsapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from slmsapp.models import CustomUser
from django.db.models import Q
from django.http import HttpResponse
from datetime import datetime
import json

from django.contrib.auth import get_user_model
User = get_user_model()

def BASE(request):
    return render(request,'base.html')

def FIRSTPAGE(request):
    return render(request,'firstpage.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password')
                                         )
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                 return redirect('admin_home')
            elif user_type == '2':
                 return redirect('staff_home')
            return redirect('index')
            
        else:
                messages.error(request,'Email ou Senha Inválido')
                return redirect('login')
    else:
            messages.error(request,'Email ou Senha Inválido')
            return redirect('login')
        


def doLogout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/')
def INDEX(request):
     return render(request,'index.html')

login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)
@login_required(login_url = '/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(profile_pic)
        

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            

            
            if profile_pic !=None and profile_pic != "":
               customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"Update Completo")
            return redirect('profile')

        except:
            messages.error(request,"Falha no Update")
    return render(request, 'profile.html')


def CHANGE_PASSWORD(request):
     context ={}
     ch = User.objects.filter(id = request.user.id)
     
     if len(ch)>0:
            data = User.objects.get(id = request.user.id)
            context["data"]:data            
     if request.method == "POST":        
        current = request.POST["cpwd"]
        new_pas = request.POST['npwd']
        user = User.objects.get(id = request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
          user.set_password(new_pas)
          user.save()
          messages.success(request,'Mudança de senha concluída')
          user = User.objects.get(username=un)
          login(request,user)
        else:
          messages.success(request,'Senha Incorreta')
          return redirect("change_password")
     return render(request,'change-password.html')

def BUSINESS_HOURS(request):
    current_hour = datetime.now().hour
    if 9 <= current_hour < 20:
        return HttpResponse("Em Expediente")
    else:
        return HttpResponse("Fora do Expediente")
    
def your_view(request):
    # Exemplo de dados mensais (ajuste conforme necessário)
    staff_monthly_data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 40]  # Exemplo de dados para funcionários
    leave_monthly_data = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # Exemplo de dados para licenças

    return render(request, 'your_template.html', {
        'staff_monthly_data': json.dumps(staff_monthly_data),
        'leave_monthly_data': json.dumps(leave_monthly_data),
    })