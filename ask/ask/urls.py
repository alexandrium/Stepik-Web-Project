"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from qa import views
from django.urls import include

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.new, name='new'),
    # path('login/', views.login, name='login'),
    path('login', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user='True'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='password_reset'),
    # path('signup/', views.signup, name='signup'),

    path('question/<int:id>/', views.detail, name='detail'),
    # re_path(r'^question/(?P<id>\d+)/$', views.detail, name='detail'),

    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='test'),
]

