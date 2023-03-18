from django.shortcuts import render

# Create your views here.
def loginForm(request):
    data={
        'title':'Member Registration'
    }
    return render(request,"registration/login.html",data)