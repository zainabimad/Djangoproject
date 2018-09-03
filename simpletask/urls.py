"""simpletask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path , include
from project import views
from Orphans import urls
from Guarantor import urls as Gua

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:id>', views.base, name="base"),
    path('', views.signor, name="login_or"),
    path('login/', views.logins, name="login"),
    path('sign/have_account/', views.have, name="account"),
    path('all_gua/', views.all_gua, name="all_gua"),
    path('delete_gua/<int:id>', views.del_gua, name="delete_gua"),
    path('all_or/', views.all_or, name="all_or"),
    path('delete_or/<int:id>', views.del_or, name="delete_or"),
    path('activities/', views.ac, name="activities"),
    path('show_ad/', views.show_all_re_ad, name="show_request_ad"),
    path('delete_act/<int:id>', views.del_act, name="delete_act"),
    path('delete_request/<int:id>', views.delete_request, name="delete_request"),
    path('accept/<int:id>', views.accept, name="accept"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('orphans/', include(urls)),
    path('guarantor/', include(Gua)),

]
