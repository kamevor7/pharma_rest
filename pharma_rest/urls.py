"""pharma_rest URL Configuration

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
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.patient_list),
    url(r'^api/patients/$', views.patient_list),
    url(r'^api/patients/(?P<pk>[0-9]+)$', views.getPatient),
    path('prescriptions/', views.prescription_list),
    url(r'^api/prescriptions/$', views.prescription_list),
    url(r'^api/prescriptions/(?P<pk>[0-9]+)$', views.getPrescription),
    path('locations/', views.location_list),
    url(r'^api/locations/$', views.location_list),
    url(r'^api/locations/(?P<pk>[0-9]+)$', views.getLocation),
]
