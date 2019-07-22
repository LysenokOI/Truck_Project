from django.shortcuts import render
from truck_app.models import TruckModel, TruckWork
# Create your views here.


def truck_info(request):
    truck_list = TruckModel.objects.all()
    choose_truck = request.POST.get('selector')

    if choose_truck == 'all':
        choose_response = TruckWork.objects.all()
    else:
        choose_response = TruckWork.objects.all().filter(
                          truck_work=choose_truck)

    truck_dict = {"truck_records": truck_list,
                  "chose_truck": choose_response}
    return render(request, "truck_app/truck_info.html", context=truck_dict)
