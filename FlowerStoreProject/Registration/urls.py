from . import views
from django.urls import  path


urlpatterns = [
    path('',views.loginForm,name="registration.login"),
    # path('',include('Registration.urls')),
]
