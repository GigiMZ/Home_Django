"""
URL configuration for Django_HW_1 project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests/', views.tests, name='tests'),
    path('test/<int:pk>', views.test_detail, name='detail-test'),
    path('create_test/', views.test_create, name='create-test'),
    path('update_test/<int:pk>', views.test_update, name='update-test'),
    path('delete_test/<int:pk>', views.test_delete, name='delete-test')
]
