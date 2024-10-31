from django.shortcuts import render
from .models import Agenda, AgendaLocation
from django.shortcuts import redirect,get_object_or_404
from .forms import *
from datetime import datetime
from datetime import timedelta
import json
import requests
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from decouple import config
from destinations.models import Destination
from django.contrib.auth.decorators import login_required


@csrf_protect
@login_required
def agenda_main(request):
    agendas = Agenda.objects.all()  # 获取所有 Agenda 实例
    return render(request, 'agenda/main.html', {'agendas': agendas})

@csrf_protect
@login_required
def agenda_calendar(request):
    return render(request, 'agenda/calendar.html')

@csrf_protect
@login_required
def agenda_map(request):
    return render(request, 'agenda/map_new.html') # zsz

@csrf_protect
@login_required
def agenda_LLM(request):
    return render(request, 'agenda/LLM.html')

@csrf_protect
@login_required
def agenda_my(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda/myagenda.html', {'agendas': agendas})

@csrf_protect
@login_required
def agenda_list(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda/agenda_list.html', {'agendas': agendas})

@csrf_protect
@login_required
def delete_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    agenda.delete()
    return redirect('agenda:agenda_list')

@csrf_protect
@login_required
def delete_agendalocation(request, id):
    loc = get_object_or_404(AgendaLocation, id=id)
    loc.delete()
    return redirect('agenda:agenda_list')
# def update_agenda(request, id):
#     agenda = get_object_or_404(Agenda, id=id)
#     if request.method == 'POST':
#         agenda_form = AgendaForm(request.POST, instance=agenda)
#         # 这里可以处理 AgendaLocation 的更新
#         if agenda_form.is_valid():
#             agenda_form.save()
#             return redirect('agenda:agenda_list')
#     else:
#         agenda_form = AgendaForm(instance=agenda)

#     return redirect('agenda:agenda_list')
    # 处理更新逻辑（例如，显示表单并保存数据）
@csrf_protect
@login_required
def update_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    if request.method == 'POST':
        agenda_form = TravelAgendaForm(request.POST, instance=agenda)
        if agenda_form.is_valid():
            agenda_form.save()
            return redirect('agenda:agenda_list')  # 更新后重定向到日程列表页面
    else:
        agenda_form = AgendaForm(instance=agenda)
    
    # 动态渲染更新页面，传递 Agenda 数据到模板
    return render(request, 'agenda/update_Travelagenda.html', {
        'agenda_form': agenda_form,
        'agenda': agenda,  # 传递当前日程对象
    })
@csrf_protect
@login_required
def update_agendalocation(request,id):
    loc = get_object_or_404(AgendaLocation, id=id)  # 获取 AgendaLocation 对象
    agenda = loc.agenda
    if request.method == 'POST':
        agenda_form = AgendaForm(request.POST, instance=loc)  # 使用 AgendaLocationForm
        if agenda_form.is_valid():
            agenda_form.save()
            return redirect('agenda:agenda_list')  # 更新后重定向到日程列表页面
    else:
        agenda_form = AgendaLocationForm(instance=loc)  # 传递当前 AgendaLocation 实例
    
    # 动态渲染更新页面，传递 AgendaLocation 数据到模板
    return render(request, 'agenda/update_agenda.html', {
        'agenda_form': agenda_form,
        'location': loc,  # 传递当前 AgendaLocation 对象
    })

@csrf_protect
@login_required
def add_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:agenda_list')  # 添加后重定向回日程列表
    else:
        form = AgendaForm()
    return render(request, 'agenda/add_agenda.html', {'form': form})
@csrf_protect
@login_required
def add_Travelagenda(request):
    if request.method == 'POST':
        
        form_1 = TravelAgendaForm(request.POST)
        if form_1.is_valid():
            form_1.save()
            return redirect('agenda:agenda_list')
        data = json.loads(request.body)
        form_2 = TravelAgendaForm(data)
        if form_2.is_valid():
            form_2.save()
            return redirect('agenda:agenda_list')
    else:
        form = TravelAgendaForm()
    return render(request, 'agenda/add_Travelagenda.html', {'form': form})

@csrf_protect
@login_required
def calendar_view(request):
    # 获取所有的 Agenda 相关数据
    agendalocations = AgendaLocation.objects.all()
    # 构建 FullCalendar 所需的事件数据
    events = []
    for agendalocation in agendalocations:
        events.append(({
            "title":f"{agendalocation.departure_location.name} - {agendalocation.arrival_location.name}",
            "start":agendalocation.departure_time.isoformat(),
            "end":agendalocation.arrival_time.isoformat(),  # 事件结束时间, 假设为到达时间2小时后
            "departure_location":agendalocation.departure_location.name,
            "arrive_location":agendalocation.arrival_location.name,
            "transportation":agendalocation.commute_info,
            }
        ))
    events_json = json.dumps(events)
    context = {
        'events': events_json
    }
    return render(request, 'agenda/calendar.html', context)

@csrf_protect
@login_required
def call_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        destination_name = data.get('destination')
        setoff_city = data.get('departure_city')
        departure_date = data.get('departure_date')
        return_date = data.get('return_date')
        play_types = data.get('play_type',[])
        hotel_price = data.get('hotel_price',[])
        must_play = data.get('must_play',[])
        text_content = ""
        PRICE_RANGES = {
        'BUDGET': (0, 400),  # 400以内
        'MID': (400, 800),  # 400-800
        'LUXURY': (800, None),  # 800以上
        'ALL': (None, None)  # No filtering if 'ALL' is selected
    }
        if hotel_price:
            price_conditions = None
            hotels_query = Destination.objects.filter(tags='HOTEL')
            for price_category in hotel_price:
                if price_category == 'ALL':
                    price_conditions = None
                    break  
                price_min, price_max = PRICE_RANGES.get(price_category, (None, None))
                if price_min is not None and price_max is not None:
                    hotels_query = hotels_query.filter(cost__gte=price_min, cost__lte=price_max)
                elif price_min is not None:
                    hotels_query = hotels_query.filter(cost__gte=price_min)
            hotels = hotels_query
            text_content += "推荐的旅馆:\n"
            for hotel in hotels:
                text_content += f"名称: {hotel.name}, 地址: {hotel.address}, 星级: {hotel.stars}\n"
            text_content += "\n"
        
        if 'FOOD' in play_types:
            text_content += "推荐的美食:\n"
            eat_shopping_destinations = Destination.objects.filter(tags__in=['EAT'])
            for destination in eat_shopping_destinations:
                text_content += f"名称: {destination.name}, 地址: {destination.address}\n"
            text_content += "\n"
        
        if 'SHOPPING' in play_types:
            text_content += "推荐的购物景点:\n"
            eat_shopping_destinations = Destination.objects.filter(tags__in=['VISIT'])
            for destination in eat_shopping_destinations:
                text_content += f"名称: {destination.name}, 地址: {destination.address}\n"
            text_content += "\n"

        if play_types:
            text_content += "推荐的游玩地点:\n"
            play_destinations = Destination.objects.filter(tags='PLAY', play_type__in=play_types)
            for play_destination in play_destinations:
                text_content += f"名称: {play_destination.name}, 地址: {play_destination.address}\n"
            text_content += "\n"
            
        with open('destination_knowledge_base.txt', 'w', encoding='utf-8') as file:
            file.write(text_content)
        
        with open('destination_knowledge_base.txt', 'r', encoding='utf-8') as file:
            knowledge_base = file.read()
        
        prompt = (
            f"请基于以下提供的信息为我设计一份详细的旅行日程规划。日程应从{departure_date}出发至{destination_name}，"
            f"在{return_date}返回。我希望能够涵盖每日的活动安排、包括游玩景点、通勤时间、通勤方式以及餐饮时间（如早餐、午餐和晚餐）。"
            f"我一定要去的地方是{must_play},请务必将它详细安排在某一天的日程规划中"
            f"此外，若有其他值得推荐的景点或活动，请一并补充到行程中。以下是相关信息：\n\n"
            f"{knowledge_base}\n\n"
            f"我偏好的游玩类型包括：{play_types}，并希望旅馆价格在{hotel_price}范围内。"
            "请根据这些信息，生成一个完整且有趣的旅行计划。"
        )


        url = 'https://spark-api-open.xf-yun.com/v1/chat/completions'  # API的URL
        
        # 创建payload，包含目的地和天数
        payload = {
            'model': 'generalv3.5',  # 指定请求的模型
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
             'stream': False  # 设置为非流式响应
        }

        bearer_token = 'PzfmyIDmgfUOEZGdLmNB:ZfmpxbVMijaJThZaVWeQ'

        # 设置请求头
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json',  # 确保请求内容为JSON格式
        }

        try:
            # 发送POST请求，传入数据和头信息
            response = requests.post(url, json=payload, headers=headers)

            # 检查响应状态码
            response.raise_for_status() 

            # 解析响应内容，假设返回结果为JSON格式
            response_data = response.json()
            result_text = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
            print(result_text)
            # 返回合并后的结果
            return JsonResponse({'result': result_text})  

        except requests.exceptions.HTTPError as err:
            # 处理HTTP错误
            return JsonResponse({'error': str(err)}, status=response.status_code)
        except Exception as e:
            # 处理其他可能的异常
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

class AgendaListView(LoginRequiredMixin, ListView):
    model = Agenda
    #model = Agenda
    template_name = 'agenda/agenda_list.html'
    context_object_name = 'agendas'
    ordering = ['-created_at']  # 根据创建时间排序
    paginate_by = 10  # 每页 10 条记录
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query = self.request.GET.get('q')
    #     if query:
    #         #queryset = queryset.filter(Q(title__icontains=query))
    #         queryset = queryset.filter(Q(departure_location__name__icontains=query)|Q(arrival_location__name__icontains=query)|Q(agenda__title__icontains=query))
    #     return queryset.values('agenda')
    @csrf_protect
    @login_required
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
    
        if query:
        # 筛选出符合条件的 AgendaLocation 实例
            # filtered_locations = queryset.filter(
            #     Q(departure_location__name__icontains=query) |
            #     Q(arrival_location__name__icontains=query) |
            #     Q(agenda__title__icontains=query)|
            #     Q(commute_info__icontains=query)
            # )   
            queryset = queryset.filter(Q(title__icontains=query))
        # 获取这些实例对应的 agenda，并去重
            #agendas = filtered_locations.values('agenda').distinct()

        # 返回符合条件的 agenda
            return queryset