from django.contrib import admin
from django.urls import path
from mlblogs.views import allmodellist
from mlblogs.views import alluserlist
from mlblogs.views import adduser
from mlblogs.views import addmodel
from mlblogs.views import allmodellist
from mlblogs import views 

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.api),
    path('alluserlist/', alluserlist,name='alluserlist'),
    path('adduser/',adduser,name="adduser"),
    path('addmodel/',addmodel,name="adduser"),
    path('allmodellist/',allmodellist,name="allmodellist")
]
