"""
URL configuration for Projet_mService project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tracking/', include('tracking.urls')),
    path('login/', include('loginn.urls')),
    path('elements/', include('elements.urls')),
    path('confirmation/', include('confirmation.urls')),
    path('checkout/', include('checkout.urls')),
    path('category/', include('category.urls')),
    path('cart/', include('cart.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('registration/', include('registration.urls')),
    path('forgotPassword/', include('forgotPassword.urls')),
    path('logout/', include('logoutt.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('createblog/', include('createblog.urls')),
    path('listproduit/', include('listproduit.urls')),
    path('modifierinfo/', include('modifierinfo.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
