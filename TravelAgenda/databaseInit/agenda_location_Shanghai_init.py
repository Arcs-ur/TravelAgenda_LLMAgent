import os
import sys
import django
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TravelAgenda.settings')
django.setup()

from agenda.models import Location

# 准备要插入的数据，在[]里面修改，记得末尾加逗号 @各位
locations = [
    Location(name='南京路', address='上海, 上海市, 黄浦区'),
    Location(name='外滩', address='上海, 上海市, 黄浦区'),
    Location(name='东方明珠', address='上海, 上海市, 浦东新区'),
    Location(name='人民广场', address='上海, 上海市, 黄浦区'),
    Location(name='陆家嘴', address='上海, 上海市, 浦东新区'),
    Location(name='田子坊', address='上海, 上海市, 卢湾区'),
    Location(name='上海博物馆', address='上海, 上海市, 黄浦区'),
    Location(name='豫园', address='上海, 上海市, 黄浦区'),
    Location(name='世纪公园', address='上海, 上海市, 浦东新区'),
    Location(name='徐家汇', address='上海, 上海市, 徐汇区'),
    Location(name='静安寺', address='上海, 上海市, 静安区'),
    Location(name='上海图书馆', address='上海, 上海市, 徐汇区'),
    Location(name='长风海洋世界', address='上海, 上海市, 普陀区'),
    Location(name='上海迪士尼乐园', address='上海, 上海市, 浦东新区'),
    Location(name='华东师范大学', address='上海, 上海市, 闵行区'),
    Location(name='博物馆', address='上海, 上海市, 静安区'),
    Location(name='南翔古镇', address='上海, 上海市, 嘉定区'),
    Location(name='上海南站', address='上海, 上海市, 闵行区'),
    Location(name='上海动物园', address='上海, 上海市, 闵行区'),
    Location(name='松江大学城', address='上海, 上海市, 松江区'),
    Location(name='虹口足球场', address='上海, 上海市, 虹口区'),
    Location(name='上海国际会议中心', address='上海, 上海市, 浦东新区'),
    Location(name='梅龙镇', address='上海, 上海市, 黄浦区'),
    Location(name='徐家汇天主教堂', address='上海, 上海市, 徐汇区'),
    Location(name='真如寺', address='上海, 上海市, 普陀区'),
    Location(name='华东理工大学', address='上海, 上海市, 徐汇区'),
    Location(name='中山公园', address='上海, 上海市, 虹口区'),
    Location(name='上海体育场', address='上海, 上海市, 徐汇区'),
    Location(name='虹口公园', address='上海, 上海市, 虹口区'),
    Location(name='陆家嘴金融区', address='上海, 上海市, 浦东新区'),
    Location(name='金茂大厦', address='上海, 上海市, 浦东新区'),
    Location(name='上海城市规划展览馆', address='上海, 上海市, 黄浦区'),
    Location(name='杨浦大桥', address='上海, 上海市, 杨浦区'),
    Location(name='浦东国际机场', address='上海, 上海市, 浦东新区'),
    Location(name='东方艺术中心', address='上海, 上海市, 浦东新区'),
    Location(name='上海世博会博物馆', address='上海, 上海市, 浦东新区'),
    Location(name='静安公园', address='上海, 上海市, 静安区'),
    Location(name='万里长征', address='上海, 上海市, 松江区'),
    Location(name='安福路', address='上海, 上海市, 徐汇区'),
    Location(name='外滩源', address='上海, 上海市, 黄浦区'),
    Location(name='新华路', address='上海, 上海市, 普陀区'),
    Location(name='奉贤海湾', address='上海, 上海市, 奉贤区'),
    Location(name='人民公园', address='上海, 上海市, 黄浦区'),
    Location(name='博物馆', address='上海, 上海市, 虹口区'),
    Location(name='长宁区', address='上海, 上海市, 长宁区'),
    Location(name='世纪大道', address='上海, 上海市, 浦东新区'),
    Location(name='世纪公园', address='上海, 上海市, 浦东新区'),
    Location(name='静安寺', address='上海, 上海市, 静安区'),
    Location(name='南翔古镇', address='上海, 上海市, 嘉定区'),
    Location(name='阳光100', address='上海, 上海市, 黄浦区'),
    Location(name='新天地', address='上海, 上海市, 卢湾区'),
    Location(name='普陀山', address='上海, 上海市, 普陀区'),
    Location(name='上海图书馆', address='上海, 上海市, 徐汇区'),
    Location(name='静安寺', address='上海, 上海市, 静安区'),
    Location(name='上海大剧院', address='上海, 上海市, 黄浦区'),
    Location(name='上海老街', address='上海, 上海市, 黄浦区'),
    Location(name='天山路', address='上海, 上海市, 长宁区'),
    Location(name='小南国', address='上海, 上海市, 黄浦区'),
    Location(name='南浦大桥', address='上海, 上海市, 浦东新区'),
    Location(name='松江广场', address='上海, 上海市, 松江区'),
    Location(name='苏州河', address='上海, 上海市, 浦东新区'),
    Location(name='浦江游船', address='上海, 上海市, 浦东新区'),
    Location(name='四平路', address='上海, 上海市, 杨浦区'),
    Location(name='复兴公园', address='上海, 上海市, 徐汇区'),
    Location(name='西藏南路', address='上海, 上海市, 黄浦区'),
    Location(name='大宁路', address='上海, 上海市, 大宁区'),
    Location(name='东昌路', address='上海, 上海市, 浦东新区'),
    Location(name='西南地区', address='上海, 上海市, 徐汇区'),
    Location(name='长江大桥', address='上海, 上海市, 宝山区'),
    Location(name='望海路', address='上海, 上海市, 宝山区'),
    Location(name='云岭东路', address='上海, 上海市, 普陀区'),
    Location(name='黄浦江', address='上海, 上海市, 黄浦区'),
    Location(name='青浦区', address='上海, 上海市, 青浦区'),
    Location(name='华东师范大学', address='上海, 上海市, 闵行区'),
    Location(name='闵行区', address='上海, 上海市, 闵行区'),
    Location(name='南方商城', address='上海, 上海市, 宝山区'),
    Location(name='华东理工大学', address='上海, 上海市, 徐汇区'),
    Location(name='东宁路', address='上海, 上海市, 浦东新区'),
    Location(name='金山区', address='上海, 上海市, 金山区'),
    Location(name='奉贤区', address='上海, 上海市, 奉贤区'),
    Location(name='松江区', address='上海, 上海市, 松江区'),
    Location(name='上海大剧院', address='上海, 上海市, 黄浦区'),
    Location(name='西安路', address='上海, 上海市, 普陀区'),
    Location(name='天潼路', address='上海, 上海市, 黄浦区'),
    Location(name='虹口区', address='上海, 上海市, 虹口区'),
    Location(name='长宁区', address='上海, 上海市, 长宁区'),
    Location(name='上海南站', address='上海, 上海市, 闵行区'),
    Location(name='漕河泾', address='上海, 上海市, 徐汇区'),
    Location(name='华东理工大学', address='上海, 上海市, 徐汇区'),
    Location(name='中兴路', address='上海, 上海市, 黄浦区'),
    Location(name='浦东国际机场', address='上海, 上海市, 浦东新区'),
    
]


# 执行批量插入
Location.objects.bulk_create(locations)

# print("Location地点数据已成功插入！")

