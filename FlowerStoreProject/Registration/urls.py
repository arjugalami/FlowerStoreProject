from . import views
from django.urls import  path


urlpatterns = [
    path('login/',views.loginForm,name="registration.login"),
    # path('',include('Registration.urls')),
    path('',views.signForm,name="registration.signup"),
    path('store/',views.registrationStore,name="registration.store"),
]
