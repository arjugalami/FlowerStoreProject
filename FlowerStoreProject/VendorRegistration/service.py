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



# for product


def productStore(request):
    product=VendorRegister(
        user_id=request.user.id,
        product_name=request.POST['product_name'],
        product_price=request.POST['product_price'],
        product_photo=request.FILES.get('product_photo',False),
        product_description=request.POST['product_description'],
        product_quantity=request.POST['product_quantity'],
        product_address=request.POST['product_address'],
        created_at=request.POST.get('created_at',False),
        updated_at=request.POST.get('updated_at',False),
        
    )
    product.save()
    return "sucess"


def productUpdate(request,id):
    product=VendorRegister.objects.get(id=id)    #yesto ko id chai form bata ako and arko chai database bata id

    product.product_name=request.POST['product_name'],
    product.product_price=request.POST['product_price'],
    product.product_photo=request.FILES.get('product_photo',False),
    product.product_description=request.POST['product_description'],
    product.product_quantity=request.POST['product_quantity'],
    product.product_address=request.POST['product_address'],
    product.created_at=request.POST.get('created_at',False),
    product.updated_at=request.POST.get('updated_at',False),
        
    product.save()
    return "sucess"

def productDelete(id):
    product = VendorRegister.objects.get(id = id)
    product.delete()
    return "success"

def getproductId(id):
    product = VendorRegister.objects.get(id= id)
    return product

def getproduct():
    product =  VendorRegister.objects.values().all()
    return list(product)