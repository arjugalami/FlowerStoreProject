from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import VendorRegister

from VendorRegistration import service


#yo page le chai controller ko kaam garya xa vendor ko login ko lagi
#template ra database ko bich ko match bhaxa kinai data
def loginForm(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('vendor.create')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'Vendor/login.html')



#yo page chai controller ko kaam garya xa vendor ko signup ko lagi
def SignupPage(request):
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')

        if password1 != password2:
            #messages.success(request, 'first password and second password is not correct!!!')
            return HttpResponse("Your password and confrom password doesnot match !!!")
        if User.objects.filter(username=username).first():
            #messages.success(request, "Such a user has already registered!!!")
            return HttpResponse('Such a user has already registered!!!')

        if User.objects.filter(email=email).first():
            #messages.success(request, "This email has already been registered!!!")
            return HttpResponse('This email has already been registered!!!')
        user_obj = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
        user_obj.set_password(raw_password=password1)
        user_obj.save()
        return redirect('vendor.login')

    return render (request,'vendor/signup.html')


#yeha dekhi vendor ko
#vendor ko lagi banako template chai mapping garxa
def vendorCreate(request):
    data={
        'title':"vendor"
    }
    return render(request,'Vendor/addVendor.html',data)



#yesle template bata leko data, database ma gayera store/save garya xa
def vendorStore(request):
   # print(request.POST)
    store= service.vendorStore(request)
    return redirect('vendor.list')



#databse ko data template ma show garya xa
def vendorList(request):
    # vendor=VendorRegister.objects.all()
    vendor=VendorRegister.objects.values().filter(user_id=request.user.id)
    data={
        'vendor':vendor
    }
    return render(request,'vendor/list.html',data)


# yo function le edit form create garya
def vendorEdit(request,id):
    vendor=service.getvendorId(id)
    data={
        'title':'product',
        # 'driver':service.getVechalId(id),
        'vendor':vendor    
    }
    return render(request,'Vendor/addVendor.html',data)


#yo function le template ko data chai database ma update garya
def vendorUpdate(request,id):
    service.vendorUpdate(request, id)
    return redirect('vendor.list')


# yo function le template chai database bata delete garxa
def vendorDelete(request,id):
    service.vendorDelete(id)
    return redirect('vendor.list')



#for product 


#product ko lagi banako template chai mapping garxa
def productCreate(request):
    data={
        'title':"product"
    }
    return render(request,'Vendor/addPrduct.html',data)



#yesle template bata leko data, database ma gayera store/save garya xa
def productStore(request):
   # print(request.POST)
    store= service.productStore(request)
    return redirect('vendor.list')



#databse ko data template ma show garya xa
def productList(request):
    # vendor=VendorRegister.objects.all()
    product=VendorRegister.objects.values().filter(user_id=request.user.id)
    data={
        'product':product
    }
    return render(request,'Vendor/list.html',data)


# yo function le edit form create garya
def productEdit(request,id):
    product=service.getproductId(id)
    data={
        'title':'product',
        # 'driver':service.getVechalId(id),
        'product':product    
    }
    return render(request,'Vendor/addProduct.html',data)


#yo function le template ko data chai database ma update garya
def productUpdate(request,id):
    service.productUpdate(request, id)
    return redirect('vendor.list')


# yo function le template chai database bata delete garxa
def productDelete(request,id):
    service.productDelete(id)
    return redirect('vendor.list')
