"""
URL configuration for movieproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from movies import views
app_name="movies"

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.Homeview.as_view(),name='home'),

    # path('add/',views.add,name='add'),
    path('add/',views.Addmovie.as_view(),name='add'),

    # path('view/<int:n>',views.view,name='view'),
    path('view/<int:pk>',views.Detail_view.as_view(),name='view'), # class based url

    # path('delete/<int:n>/',views.delete,name='delete'),
    path('delete/<int:pk>/',views.Delete_view.as_view(),name='delete'),

    # path('update/<int:n>/',views.update,name='update')
    path('update/<int:pk>/',views.Update_view.as_view(),name='update')
]
