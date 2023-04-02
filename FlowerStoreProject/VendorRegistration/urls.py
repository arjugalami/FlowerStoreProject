from . import views
from django.urls import  path


urlpatterns = [
    path('VendorLogin/',views.loginForm,name="vendor.login"),
    # path('',include('Registration.urls')),
    path('VendorLogin/',views.SignupPage,name="vendor.signup"),
    path('store/',views.vendorStore,name="vendor.store"),   
    path('list/', views.vendorList, name='vendor.list'),
    # path('store', views.vechalStore,name='driver.store'),
    path('add', views.vendorCreate,name='vendor.create'),
    path('edit/<int:id>', views.vendorEdit,name='vendor.edit'),
    path('delete/<int:id>', views.vendorDelete,name='vendor.delete'),
    path('update/<int:id>', views.vendorUpdate,name='vendor.update'),

]


