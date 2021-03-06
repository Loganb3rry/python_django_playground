"""python_django_playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('accounts/login/', views.LoginView.as_view, name='login'),
    path('accounts/logout/', views.LogoutView.as_view, name='logout', kwargs={'next_page': '/'}),

    # path('', views.IndexView.as_view(), name='index'),
    # path('school_app/', include('school_app.urls', namespace='school_app'))
    # path('user_app/', include('users_app.urls')),
    # path('logout/', views.user_logout, name='logout'),
]
