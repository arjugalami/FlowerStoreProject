from . import views
from django.urls import  path


urlpatterns = [
    path('login/',views.LoginForm,name="registration.login"),
    # path('',include('Registration.urls')),
    path('signup/',views.SignUpForm,name="registration.signup"),
    #path('store/',views.registrationStore,name="registration.store"),
    path('',views.FirstPage, name="first"),

]
