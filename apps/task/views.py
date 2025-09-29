from django.shortcuts import render,redirect

from .models import User,City
from zoneinfo import ZoneInfo
from datetime import datetime


# Create your views here.
def welcom_page(request):
    return render(request,"index.html")

def list_user(request):
    users = User.objects.all()
    return render(request,"users.html",{"users":users})


def cities(request):
    cities = City.objects.all()
    return render(request,"cities.html",{"cities":cities})

def cities_time(request):
    cities = City.objects.all()
    city_times = []
    
    for city in cities:
        tz = ZoneInfo(city.timezone)
        now = datetime.now(tz)
        city_times.append({
            "name":city.name,
            "time":now.strftime("%H:%M:%S")
        })
    return render(request,"city_time.html",{"city_times":city_times})


def Counter(request):
    if "counter" not in request.session:
        request.session["counter"]=0
    return render(request, "counter.html",{"counter":request.session["counter"]})


def inc_counter(request):
    request.session["counter"] = request.session.get("counter",0)+1
    return redirect("counter")


def reset_counter(request):
    request.session["counter"]=0
    return redirect("counter")
