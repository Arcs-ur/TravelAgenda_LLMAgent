from django import forms
from .models import Agenda, Location, AgendaLocation

class AgendaForm(forms.ModelForm):
    # 通过字段添加与 `AgendaLocation` 相关的内容
    departure_location = forms.ModelChoiceField(queryset=Location.objects.all(), label="出发地")
    arrival_location = forms.ModelChoiceField(queryset=Location.objects.all(), label="目的地")
    arrival_time = forms.DateTimeField(label="到达时间", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    commute_info = forms.CharField(widget=forms.Textarea, label="通勤信息")

    class Meta:
        model = AgendaLocation
        fields = ['agenda', 'departure_location','arrival_location', 'arrival_time', 'commute_info']
    
    # 根据需求，可以在初始化时做更多自定义设置或数据的动态调整
    def __init__(self, *args, **kwargs):
        super(AgendaForm, self).__init__(*args, **kwargs)
        # 在这里可以进一步修改字段或设置默认值

class TravelAgendaForm(forms.ModelForm):
    # 通过字段添加与 `AgendaLocation` 相关的内容
    # departure_location = forms.ModelChoiceField(queryset=Location.objects.all(), label="出发地")
    # arrival_location = forms.ModelChoiceField(queryset=Location.objects.all(), label="目的地")
    # arrival_time = forms.DateTimeField(label="到达时间", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    # commute_info = forms.CharField(widget=forms.Textarea, label="通勤信息")

    class Meta:
        model = Agenda
        fields = ['title']
    
    # 根据需求，可以在初始化时做更多自定义设置或数据的动态调整
    def __init__(self, *args, **kwargs):
        super(TravelAgendaForm, self).__init__(*args, **kwargs)
        # 在这里可以进一步修改字段或设置默认值