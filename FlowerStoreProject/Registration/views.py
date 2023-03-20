from django.http import HttpResponse
from django.shortcuts import render,redirect

from Registration.models import Registration

# Create your views here.
def loginForm(request):
    data={
        'title':'Member Registration'
    }
    return render(request,"registration/login.html",data)

def signForm(request):
    data={
        'title':'signup'
    }
    return render(request,"registration/signup.html",data)
def registrationStore(request):
    if request.method=='POST':
        password=request.POST['password'] # your password is stored in varaible "password"
        cpassword=request.POST['cpassword']

        if password != cpassword:
            return HttpResponse("Your password and confirm password does not match")
        
        else:
            registration = Registration(
                email = request.POST['email'], #registration is a variable where models ko 'Registration' class ho. email bhanne chai form ko same hunu paryo.
                full_name = request.POST['full_name'],
              
                password = request.POST['password'],
                confirm_password = request.POST['cpassword'],
                created_at = request.POST.get('created_at',False), #kei karan le data store bhayena bhane false garne
                updated_at = request.POST.get('updated_at',False)

            )
            registration.save()
            return redirect('registration.login')
    return render(request,'registration/signup.html')