"""warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from warehouse_app.views import UserAPIView, CategoryAPIView, LocationAPIView, ProductAPIView, PhotoAPIView, SpecificCategoryAPIView, SpecificLocationAPIView, SpecificProductAPIView, SpecificPhotoAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('category/', SpecificCategoryAPIView.as_view()),
    path('locations/', LocationAPIView.as_view()),
    path('location/', SpecificLocationAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('product/', SpecificProductAPIView.as_view()),
    path('photos/', PhotoAPIView.as_view()),
    path('photo/<int:pk>/', SpecificPhotoAPIView.as_view()),
]
