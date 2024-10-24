from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import call_api
app_name = 'agenda'
urlpatterns = [
    path('', views.agenda_main, name='main'),
    # path('calendar', views.agenda_calendar, name='calendar'),
    path('calendar', views.calendar_view, name='calendar'),
    path('calendar_view', views.calendar_view, name='calendar_view'),
    path('LLM', views.agenda_LLM, name='LLM'),
    path('map', views.agenda_map, name='map'),
    path('agendas/list', views.agenda_list, name='agenda_list'),
    path('agendas/delete/<int:id>/', views.delete_agenda, name='delete_agenda'),
    path('agendas/update/<int:id>/', views.update_agenda, name='update_agenda'),
    path('agendas/deleteloc/<int:id>/', views.delete_agendalocation, name='delete_agendalocation'),
    path('agendas/updateloc/<int:id>/', views.update_agendalocation, name='update_agendalocation'),
    path('myagenda', views.agenda_my, name='myagenda'),
    path('myagenda_find',views.AgendaListView.as_view(),name = 'agenda_find'),
    path('agendas/add/', views.add_agenda, name='add_agenda'),
    path('agendas/addtrip/', views.add_Travelagenda, name='add_Travelagenda'),
    path('update/<int:id>/', views.update_agenda, name='update_agenda'),
    path('call_api/', call_api, name='call_api'),
]
