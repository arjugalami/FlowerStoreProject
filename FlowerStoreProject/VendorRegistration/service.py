from .models import VendorRegister


def vendorStore(request):
    vendor=VendorRegister(
        user_id=request.user.id,
        vendor_name=request.POST['vendor_name'],
        vendor_photo=request.FILES.get('vendor_photo',False),
        vendor_email=request.POST['vendor_email'],
        vendor_location=request.POST['vendor_location'],
        created_at=request.POST.get('created_at',False),
        updated_at=request.POST.get('updated_at',False),
        
    )
    vendor.save()
    return "sucess"


def vendorUpdate(request,id):
    vendor=VendorRegister.objects.get(id=id)    #yesto ko id chai form bata ako and arko chai database bata id
    vendor.vendor_name = request.POST['vendor_name']
    vendor.vendor_photo=request.FILES.get('vendor_photo',False)
    vendor.vendor_email= request.POST['vendor_email']
    vendor.vendor_location=request.POST['vendor_location']
    vendor.created_at=request.POST.get('created_at',False)
    vendor.updated_at=request.POST.get('updated_at',False)
    vendor.save()
    return "sucess"

def vendorDelete(id):
    vendor = VendorRegister.objects.get(id = id)
    vendor.delete()
    return "success"

def getvendorId(id):
    vendor = VendorRegister.objects.get(id= id)
    return vendor

def getvendor():
    vendor =  VendorRegister.objects.values().all()
    return list(vendor)