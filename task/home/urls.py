"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    # pages using django ORM
    
    path('admin/', admin.site.urls),
    path('',homefn),
    path('status/<int:c_id>',catfn),
    path('add/',addfn),
    path('view/<int:s_id>',viewfn),
    path('deleteproduct/<int:p_id>',deleteproduct),
    path('editproduct/<int:p_id>',editproduct),
    path('login/',loginfn),
    path('register/',regfn),
    path('logout/',logoutfn),

    # api

    path('api/task/',taskapifn),
    path('api/task/<int:t_id>/',viewtaskapifn),
    path('api/task/add/',addtaskapifn),
    path('api/task/update/<int:t_id>/',updatetaskapifn),
    path('api/task/delete/<int:t_id>/',deletetaskapifn),


    # pages using fetch

    path('home2/',homefn2),
    path('view2/<int:s_id>',viewfn2),
    path('add2/',addfn2),
    path('deleteproduct2/<int:p_id>',deleteproduct2),
    path('editproduct2/<int:p_id>',editproduct2),
    path('status2/<int:c_id>',catfn2),


]
