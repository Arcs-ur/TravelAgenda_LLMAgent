from django.shortcuts import render
from django.views.generic import ListView
from .models import Destination
# 主页视图
def destination_main(request):
    return render(request, 'destinations/main.html')

# 酒店视图
def destination_hotel(request):
    return render(request, 'destinations/hotel.html')

# 餐厅视图
def destination_restaurant(request):
    return render(request, 'destinations/restaurant.html')

# 商店视图
def destination_shop(request):
    return render(request, 'destinations/shop.html')

# 景点视图
# def destination_attraction(request):
#     return render(request, 'destinations/attraction.html')
class AttractionListView(ListView):
    model = Destination
    template_name = 'destinations/attraction.html' 
    context_object_name = 'destinations'  
    paginate_by = 10  
# 交通视图
def destination_traffic(request):
    return render(request, 'destinations/traffic.html')
