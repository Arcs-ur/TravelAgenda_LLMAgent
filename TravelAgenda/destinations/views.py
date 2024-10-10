from django.shortcuts import render

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
def destination_attraction(request):
    return render(request, 'destinations/attraction.html')

# 交通视图
def destination_traffic(request):
    return render(request, 'destinations/traffic.html')
