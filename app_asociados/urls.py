"""
URL configuration for app_asociados project.

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
from panel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oficinas',views.OficinaListView.as_view(), name='oficinas-list'),
    path('oficinas/<int:pk>/detail/', views.OficinaDetailView.as_view(), name='oficinas-detail'),
    path('asociados',views.AsociadosListView.as_view(), name='asociados-list'),
    path('asociados/<int:pk>/detail/', views.AsociadosDetailView.as_view(), name='asociados-detail'),
    path('aportes',views.AporteListView.as_view(), name='asociados-list'),
    path('aportes/<int:pk>/detail/', views.AporteDetailView.as_view(), name='aportes-detail'),

    # Update
    path('asociados/<int:pk>/update/',views.AsociadosUpdate.as_view(),name='asociados-update'), 
    #Create
    path('asociados/create/', views.AsociadosCreate.as_view(), name='asociados-create'),
    #Delete
    path('asociados/<int:pk>/delete/', views.AsociadosDelete.as_view(), name='asociados-delete'),

    # Update team
    path('oficinas/<int:pk>/update/',views.OficinaUpdate.as_view(),name='oficinas-update'), 
    #Create oficinas
    path('oficinas/create/', views.OficinaCreate.as_view(), name='oficinas-create'),
    #Delete oficinas
    path('oficinas/<int:pk>/delete/', views.OficinaDelete.as_view(), name='oficinas-delete'),

    # Update team
    path('aportes/<int:pk>/update/',views.AporteUpdate.as_view(),name='aportes-update'), 
    #Create aportes
    path('aportes/create/', views.AporteCreate.as_view(), name='aportes-create'),
    #Delete aportes
    path('aportes/<int:pk>/delete/', views.AporteDelete.as_view(), name='aportes-delete'),
]
