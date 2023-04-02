# from .models import RegisterVechel


# def storVechal(request):
#     vechal=RegisterVechel(
#         vechel_no=request.POST['vechel_no'],
#         vechel_type=request.POST['vechel_type'],
#         driver_name=request.POST['driver_name'],
#         driver_licence_no=request.POST['driver_licence_no'],
#         driver_photo=request.FILES.get('driver_photo',False),
#         licence_photo=request.FILES.get('licence_photo',False),
#         created_at=request.POST.get('created_at',False),
#         updated_at=request.POST.get('updated_at',False),
        
#     )
#     vechal.save()
#     return "sucess"


# def updateVechal(request,id):
#     vechal=RegisterVechel.objects.get(id=id)
#     vechal.vechel_no = request.POST["vechel_no"]
#     vechal.vechel_type=request.POST["vechel_type"]
#     vechal.driver_name= request.POST['driver_name']
#     vechal.driver_licence_no=request.POST['driver_licence_no']
#     vechal.driver_photo=request.FILES.get('driver_photo',False)
#     vechal.licence_photo=request.FILES.get('licence_photo',False)
#     vechal.created_at=request.POST.get('created_at',False)
#     vechal.updated_at              =request.POST.get('updated_at',False)
#     vechal.save()
#     return "sucess"

# def deleteVechal(id):
#     vechal = RegisterVechel.objects.get(id = id)
#     vechal.delete()
#     return "success"

# def getVechalId(id):
#     vechal = RegisterVechel.objects.get(id= id)
#     return vechal

# def getVechal():
#     vechal =  RegisterVechel.objects.values().all()
#     return list(vechal)