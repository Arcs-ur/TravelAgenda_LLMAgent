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

def destination_attraction(request):
    # 获取查询参数
    district_query = request.GET.get('district', '')  # 获取district参数
    stars_query = request.GET.get('stars', '')  # 获取stars参数
    print(district_query)
    print(stars_query)
    
    # 获取所有目的地的查询集
    destinations = Destination.objects.all()

    # 如果提供了district查询参数，则过滤目的地
    if district_query:
        destinations = destinations.filter(address__icontains=district_query)
    

    # 如果提供了stars查询参数，则过滤目的地
    if stars_query:
        try:
            stars = int(stars_query)
            destinations = destinations.filter(stars__gte=stars)
        except ValueError:
            pass  # 处理非数字的stars输入
    
    
    print(destinations)

    # 将过滤后的目的地列表传递给模板
    context = {
        'destinations': destinations,
    }
    return render(request, 'destinations/attraction.html', context)

class AttractionListView(ListView):
    model = Destination
    template_name = 'destinations/attraction.html' 
    context_object_name = 'destinations'  
    paginate_by = 10  
# 交通视图
def destination_traffic(request):
    return render(request, 'destinations/traffic.html')
