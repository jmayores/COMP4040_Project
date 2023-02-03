"""term_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from register import views as v

from MyMoments import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('', include('django.contrib.auth.urls')),

    path('MyMoments/', views.mymoments_list_view, name='MyMoments-list'),
    path('MyMoments/<int:id>/', views.mymoments_view, name='MyMoments-detail'),
    path('', views.mymoments_create_view, name='home'),
    path('MyMoments/<int:id>/update/', views.mymoments_update_view, name='MyMoments-update'),
    path('MyMoments/<int:id>/delete/', views.mymoments_delete_view, name='MyMoments-delete')
]
