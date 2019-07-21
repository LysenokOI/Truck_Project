from django.http import HttpResponse
from django.shortcuts import render
from truck_app.models import TruckModel, TruckWork
# Create your views here.


def index(request):
    return HttpResponse("Truck index page")


def truck_info(request):
    truck_list = TruckWork.objects.order_by('cargo_weight')
    truck_dict = {"truck_records": truck_list}
    return render(request, "truck_app/truck_info.html", context=truck_dict)
