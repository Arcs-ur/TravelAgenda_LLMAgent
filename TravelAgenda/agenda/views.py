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
    form = AgendaForm()
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:agenda_list')  # 添加后重定向回日程列表
    return render(request, 'agenda/add_agenda.html', {'form': form})

@csrf_protect
@login_required

def import_agenda(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("hello",data)
        agenda_title = data.get('agenda')
        agenda_instance = Agenda.objects.create(title = agenda_title)
        itinerary_str = data.get('itinerary')

        itinerary_str = '\'' + str(itinerary_str) + '\''
        print("hi",itinerary_str)
        try:
            # 将 itinerary 字符串解析为 Python 对象
            cleaned_text = itinerary_str.replace(" ", "").replace('```json', '').replace('```', '').replace('\\\"', '\"').replace('\'', '').replace('\"[', '[').replace(']\"', ']').replace('[,"', '[').replace('{,"', '{"').replace(',,', ',').replace(',]', ']')
            #cleaned_text = cleaned_text.replace(',]', ']').replace(" ", "").replace('```json', '').replace('```', '').replace('\\\"', '\"').replace('\'', '').replace('\"[', '[').replace(']\"', ']').replace('[,"', '[').replace(',"', "\"").replace(',,', ',')
            cleaned_text = cleaned_text.replace(',}', "}").replace('[,', "[").replace("},", "},").replace("],", "],")
            print(cleaned_text)
            itinerary = json.loads(cleaned_text)
            
            for day_info in itinerary:  # 遍历列表中的第一个字典
                for day, items in day_info.items():  # 遍历字典中的每一天
                    for item in items:  # 遍历每一天的行程
                        departure_location_name = item.get('departure_location')
                        arrival_location_name = item.get('arrival_location')
                        departure_time = item.get('departure_time')
                        arrival_time = item.get('arrival_time')
                        commute_info = item.get('commute_info')
                        parsed_arrival_time = datetime.strptime(arrival_time, '%Y-%m-%d%H:%M')
                        formatted_arr_time = parsed_arrival_time.strftime('%Y-%m-%d %H:%M')
                        parsed_dep_time = datetime.strptime(departure_time, '%Y-%m-%d%H:%M')
                        formatted_dep_time = parsed_dep_time.strftime('%Y-%m-%d %H:%M')
            # 检查出发地和目的地是否存在
                        if departure_location_name and arrival_location_name:
                            AgendaLocation.objects.create(
                                agenda=agenda_instance,
                                departure_location=departure_location_name,
                                arrival_location=arrival_location_name,
                                departure_time=formatted_dep_time,
                                arrival_time=formatted_arr_time,
                                commute_info=commute_info
                            )
                        else:
                            return JsonResponse({'success': False, 'error': '地点不存在'}, status=400)
            
            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': '无效的日程格式'}, status=400)

    return JsonResponse({'success': False, 'error': '请求方式不正确'}, status=400)
# def import_agenda(request):
#     if request.method == 'POST':
#         try:
#             # 从请求体中解析 JSON 数据
#             data = json.loads(request.body)

#             # 将 JSON 数据转为表单数据
#             form = AgendaForm(data)

#             # 验证表单
#             if form.is_valid():
#                 form.save()
#                 return JsonResponse({'message': 'Agenda imported successfully.'}, status=201)

#             # 如果表单无效，返回错误信息
#             return JsonResponse({'errors': form.errors}, status=402)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

#     # 处理其他请求方式（如 GET）时可以返回一个空表单
#     form = AgendaForm()
#     return render(request, 'agenda/add_agenda.html', {'form': form})

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
            "title":f"{agendalocation.departure_location} - {agendalocation.arrival_location}",
            "start":agendalocation.departure_time.isoformat(),
            "end":agendalocation.arrival_time.isoformat(),  # 事件结束时间, 假设为到达时间2小时后
            "departure_location":agendalocation.departure_location,
            "arrive_location":agendalocation.arrival_location,
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
def location_search(request):
    if request.is_ajax() and request.method == "GET":
        query = request.GET.get('q', '')
        locations = Location.objects.filter(name__icontains=query)[:10]
        results = [{'id': loc.id, 'name': loc.name} for loc in locations]
        return JsonResponse({'items': results})

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
        '400以内': '400以内',  # 400以内
        '400到800': '400到800',  # 400-800
        '800以上': '800以上',  # 800以上
        '都可以': '都可以'  # No filtering if 'ALL' is selected
    }
        if hotel_price:
            price_conditions = None
            hotels_query = Destination.objects.filter(tags='HOTEL')
            hotel_price = '400以内'
            
        
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
            
        # with open('destination_knowledge_base.txt', 'w', encoding='utf-8') as file:
        #     file.write(text_content)
        
        # with open('destination_knowledge_base.txt', 'r', encoding='utf-8') as file:
        #     knowledge_base = file.read()
        #2024.11.01到2024.11.02，预计从温州出发，到南京游玩，我很想去中山陵，我的酒店预算每天在200~400元。
        prompt = (

            f"{departure_date}到{return_date},预计从{setoff_city}出发，到{destination_name}游玩，我很想去{must_play}，我酒店的预算在每天{hotel_price}"
            
        )


        url = 'https://spark-api-open.xf-yun.com/v1/chat/completions'  # API的URL
        
        # 创建payload，包含目的地和天数
        payload = {
            'model': 'generalv3.5',  # 指定请求的模型
            'messages': [
                {
                    'role':'system','content':'你是一个严格按照格式来生成内容的人。禁止生成任何的“\”符号！！！！！禁止生成任何的换行符！！！！！需要根据给出的地点，时间等信息来给出一份旅游攻略，其中涉及到的地点、交通方式、时间、酒店、饭店等信息必须准确详细。每一份旅游计划内部的小行程，应当按照<departure_location:xxx><departure_time:xxx><arrival_location><arrival_time><commute_info:xxx>来严格输出，并组织成json格式，输出是去除开头的```json和结尾的```。此外我要求，涉及到地点的必须具体，不能模糊只出现城市名，应当写出具体的站名。酒店饭店等也需要在行程中体现，json文件格式为day_0，day_1，day_2，……，每一天中的每一个元素组均由<departure_location:xxx><departure_time:xxx><arrival_location><arrival_time><commute_info:xxx>来严格输出。而不是单独的出现。涉及到交通方式应当写出具体的班次和时间。一个景点不应反复出现。用中文回答。'
                    
                },
                {
                    'role':'user','content': prompt
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
        
@csrf_protect
@login_required
def dashboard(request):
    agendas = Agenda.objects.all()
    return render(request, 'dashboard.html', {'agendas': agendas})
