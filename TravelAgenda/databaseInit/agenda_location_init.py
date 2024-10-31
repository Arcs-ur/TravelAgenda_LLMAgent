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
    Location(name='Daluo Mountain', address='Zhejiang,Wenzhou,Ouhai'),
    Location(name='Five Horses Street', address='Zhejiang,Wenzhou,Lucheng'),
    Location(name='Taiping Ancient Street', address='Zhejiang,Taizhou,Wenling'),
]

# 执行批量插入
Location.objects.bulk_create(locations)

print("Location地点数据已成功插入！")

