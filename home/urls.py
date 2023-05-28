
from home import views
from django.urls import path,include
from .views import doctorRerTest,loadregister
urlpatterns = [
    path('register/',views.doctorRerTest,name="register"),
    path('load/',views.loadregister,name='load')
]