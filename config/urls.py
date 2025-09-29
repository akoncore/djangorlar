"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from apps.task.views import welcom_page,list_user,cities,cities_time,Counter,inc_counter,reset_counter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=welcom_page,name="welcom_page"),
    path('users/',view=list_user),
    path('cities/',view=cities),
    path('city_time/',view = cities_time),
    path('cnt/',view = Counter, name = "counter"),
    path('cnt/inc_counter/',view = inc_counter,name = "inc_counter"),
    path('cnt/reset_counter/',view = reset_counter, name = "reset_counter")
]
