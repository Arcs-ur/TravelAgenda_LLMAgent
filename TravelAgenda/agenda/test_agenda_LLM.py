import re

agenda_text = """基于您提供的信息，以下是为您设计的旅行日程规划。请注意，由于我无法访问实时数据或特定网站的详细信息，以下信息是基于一般情况和推荐构建的，可能需要根据实际情况进行调整。

### 2024-11-05（星期二）：抵达深圳

**上午：**
- 08:00 AM - 从您的出发地搭乘飞机前往深圳宝安国际机场。
- 10:30 AM - 到达深圳宝安国际机场，完成入境手续后，乘坐出租车或地铁前往预订的酒店。

**下午：**
- 12:30 PM - 在酒店附近的餐厅享用午餐。
- 02:00 PM - 入住酒店，稍作休息。

**晚上：**
- 06:00 PM - 前往深圳最著名的景点之一——深圳湾公园，欣赏城市天际线和日落。
- 08:00 PM - 在深圳湾公园附近享用晚餐。
- 10:00 PM - 返回酒店休息。

### 2024-11-06（星期三）：探索深圳市区

**上午：**
- 07:00 AM - 在酒店享用早餐。
- 08:30 AM - 参观深圳市民中心，了解深圳的城市规划和发展。
- 10:30 AM - 前往深圳博物馆，深入了解深圳的历…
- 08:30 AM - 乘坐地铁或出租车前往深圳东部华侨城。
- 10:00 AM - 参观大侠谷生态公园，享受户外活动和自然风光。

**下午：**
- 01:00 PM - 在东部华侨城内部的餐厅享用午餐。
- 02:30 PM - 游览茶溪谷，体验中国传统文化和茶文化。
- 05:30 PM - 返回市区。

**晚上：**
- 07:00 PM - 在深圳市区享用晚餐。
- 09:00 PM - 返回酒店休息。

### 2024-11-09（星期六）：购物与返程

**上午：**
- 07:00 AM - 在酒店享用早餐。
- 08:30 AM - 前往深圳著名的购物区，如福田CBD或罗湖商业城，购买纪念品。
- 11:30 AM - 在购物区享用午餐。

**下午：**
- 01:30 PM - 返回酒店收拾行李。
- 03:00 PM - 根据返程航班时间，提前前往深圳宝安国际机场。
- 05:30 PM - 搭乘飞机返回出发地。

请根据实际情况调整行程，并提前预订酒店和机票以确保顺利出行。希望这个旅行计划能为您提供一个愉快的深圳之旅！"""

def extract_itinerary(agenda):
    itinerary = []
    current_date = ""
    lines = agenda.splitlines()

    current_destination = ""
    for line in lines:
        # 提取日期
        date_match = re.match(r'### (\d{4}-\d{2}-\d{2})', line)
        if date_match:
            current_date = date_match.group(1)
            continue
        
        # 提取时间
        time_matches = re.findall(r'(\d{1,2}:\d{2} (?:AM|PM))', line)
        if time_matches:
            time = time_matches[0]  # 取第一个时间
            # 提取出发地和目的地
            if "前往" in line or "返回" in line or "在" in line:
                destination_match = re.search(r'(?:前往|返回|在)(.*)', line)
                if destination_match:
                    current_destination = destination_match.group(1).strip()
                    itinerary.append(f"<{time}><{current_destination}>")
                else:
                    itinerary.append(f"<{time}><{current_destination}>")
    
    return itinerary

result = extract_itinerary(agenda_text)
for item in result:
    print(item)
