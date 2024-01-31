"""
URL configuration for server project.

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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.homepage),
    path('admin/', admin.site.urls),
    # path('login', views.login),
    path('signup/', views.signup, name='signup'),
    path('test_token/', views.test_token, name='test_token'),
    # path('profile/', views.view_profile, name='view_profile'),
    path('login/', views.login_view, name='login'),
    path('profile/logout', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/changepassword', views.change_password, name='change_password'),
    path('accounts/login/', views.login_view, name='login'),
    # path('accounts/', include('django.contrib.auth.urls')),  # Include other auth URLs
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)