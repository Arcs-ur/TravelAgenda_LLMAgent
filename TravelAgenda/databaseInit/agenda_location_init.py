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
    Location(name='西湖', address='浙江,杭州,西湖区'),
    Location(name='东方明珠', address='上海,上海,浦东新区'),
    Location(name='南京总统府', address='江苏,南京,玄武区'),
    Location(name='乌镇', address='浙江,嘉兴,桐乡'),
    Location(name='周庄', address='江苏,苏州,昆山市'),
    Location(name='南浔古镇', address='浙江,湖州,南浔区'),
    Location(name='秦淮河', address='江苏,南京,秦淮区'),
    Location(name='灵隐寺', address='浙江,杭州,西湖区'),
    Location(name='太湖', address='江苏,无锡,宜兴'),
    Location(name='杭州湾跨海大桥', address='浙江,杭州,萧山区'),
    Location(name='西塘古镇', address='浙江,嘉兴,嘉善'),
    Location(name='苏州园林', address='江苏,苏州,姑苏区'),
    Location(name='南京博物院', address='江苏,南京,玄武区'),
    Location(name='上海博物馆', address='上海,上海,黄浦区'),
    Location(name='黄山', address='安徽,黄山,黄山区'),
    Location(name='千岛湖', address='浙江,淳安,千岛湖镇'),
    Location(name='新天鹅堡', address='江苏,常州,溧阳市'),
    Location(name='扬州瘦西湖', address='江苏,扬州,广陵区'),
    Location(name='南通濠河', address='江苏,南通,崇川区'),
    Location(name='无锡灵山大佛', address='江苏,无锡,滨湖区'),
    Location(name='杭州宋城', address='浙江,杭州,西湖区'),
    Location(name='平江路', address='江苏,苏州,姑苏区'),
    Location(name='常熟沙家浜', address='江苏,常熟,沙家浜'),
    Location(name='天目山', address='浙江,杭州,淳安'),
    Location(name='镇江金山寺', address='江苏,镇江,润州区'),
    Location(name='宁波天一阁', address='浙江,宁波,海曙区'),
    Location(name='嘉兴南湖', address='浙江,嘉兴,南湖区'),
    Location(name='滁州琅琊山', address='安徽,滁州,琅琊区'),
    Location(name='宣城古城', address='安徽,宣城,宣州区'),
    Location(name='绍兴鲁迅故里', address='浙江,绍兴,越城区'),
    Location(name='嘉峪关', address='甘肃,嘉峪关,嘉峪关市'),
    Location(name='天台山', address='浙江,台州,天台县'),
    Location(name='安徽博物院', address='安徽,合肥,包河区'),
    Location(name='吴江同里', address='江苏,苏州,吴江区'),
    Location(name='南翔古镇', address='上海,上海,嘉定区'),
    Location(name='龙门石窟', address='河南,洛阳,龙门区'),
    Location(name='莲花山', address='浙江,温州,龙湾区'),
    Location(name='大明山', address='浙江,金华,东阳'),
    Location(name='唐家湾', address='广东,珠海,香洲区'),
    Location(name='花果山', address='江苏,连云港,连云区'),
    Location(name='阳澄湖', address='江苏,苏州,阳澄湖镇'),
    Location(name='黄龙洞', address='湖南,张家界,武陵源'),
    Location(name='东极岛', address='浙江,温州,文成县'),
    Location(name='小鱼山', address='浙江,温州,鹿城区'),
    Location(name='平湖秋月', address='浙江,杭州,西湖区'),
    Location(name='安吉竹海', address='浙江,湖州,安吉'),
    Location(name='西溪湿地', address='浙江,杭州,西湖区'),
    Location(name='张家界国家森林公园', address='湖南,张家界,武陵源'),
    Location(name='长白山', address='吉林,白山,长白山'),
    Location(name='桃花源', address='湖南,常德,桃源'),
    Location(name='太湖边', address='江苏,无锡,滨湖区'),
    Location(name='东极岛', address='浙江,温州,温州市'),
    Location(name='东极岛', address='浙江,温州,温州市'),
    Location(name='水乡乌镇', address='浙江,嘉兴,桐乡'),
    Location(name='湖州南浔', address='浙江,湖州,南浔'),
    Location(name='太湖', address='江苏,无锡,宜兴'),
    Location(name='杭州西溪湿地', address='浙江,杭州,西湖区'),
    Location(name='苏州拙政园', address='江苏,苏州,姑苏区'),
    Location(name='浙江海宁', address='浙江,嘉兴,海宁'),
    Location(name='泰州溱湖', address='江苏,泰州,泰兴'),
    Location(name='宁波慈溪', address='浙江,宁波,慈溪'),
    Location(name='宁波东极岛', address='浙江,宁波,鄞州区'),
    Location(name='九溪烟树', address='浙江,杭州,西湖区'),
    Location(name='安吉大竹海', address='浙江,湖州,安吉'),
    Location(name='常熟沙家浜', address='江苏,常熟,沙家浜'),
    Location(name='南浔古镇', address='浙江,湖州,南浔'),
    Location(name='婺源', address='江西,上饶,婺源县'),
    Location(name='黄山', address='安徽,黄山,黄山区'),
    Location(name='屯溪老街', address='安徽,黄山,屯溪区'),
    Location(name='三清山', address='江西,上饶,三清山'),
    Location(name='婺源篁岭', address='江西,上饶,婺源县'),
    Location(name='老街', address='浙江,绍兴,越城区'),
    Location(name='天目山', address='浙江,杭州,淳安'),
    Location(name='温州东极岛', address='浙江,温州,文成县'),
    Location(name='温州鹿城', address='浙江,温州,鹿城区'),
    Location(name='宁波东极岛', address='浙江,宁波,慈溪'),
    Location(name='浦江', address='浙江,金华,浦江'),
    Location(name='临安', address='浙江,杭州,临安区'),
    Location(name='崇明', address='上海,上海,崇明区'),
    Location(name='余杭', address='浙江,杭州,余杭区'),
    Location(name='奉贤', address='上海,上海,奉贤区'),
    Location(name='光明', address='浙江,嘉兴,秀洲区'),
    Location(name='南通', address='江苏,南通,通州区'),
     Location(name='天安门广场', address='北京,北京,东城区'),
    Location(name='故宫博物院', address='北京,北京,东城区'),
    Location(name='颐和园', address='北京,北京,海淀区'),
    Location(name='长城', address='北京,北京,昌平区'),
    Location(name='北京动物园', address='北京,北京,海淀区'),
    Location(name='南锣鼓巷', address='北京,北京,东城区'),
    Location(name='王府井', address='北京,北京,东城区'),
    Location(name='鸟巢', address='北京,北京,朝阳区'),
    Location(name='水立方', address='北京,北京,朝阳区'),
    Location(name='天坛公园', address='北京,北京,崇文区'),
    Location(name='798艺术区', address='北京,北京,朝阳区'),
    Location(name='香山公园', address='北京,北京,海淀区'),
    Location(name='北海公园', address='北京,北京,西城区'),
    Location(name='圆明园', address='北京,北京,海淀区'),
    Location(name='北京欢乐谷', address='北京,北京,丰台区'),
    Location(name='东直门', address='北京,北京,东城区'),
    Location(name='北京科技馆', address='北京,北京,朝阳区'),
    Location(name='明十三陵', address='北京,北京,昌平区'),
    Location(name='崇文门', address='北京,北京,崇文区'),
    Location(name='白洋淀', address='河北,保定,安新县'),
    Location(name='唐山地震遗址', address='河北,唐山,路北区'),
    Location(name='秦皇岛山海关', address='河北,秦皇岛,山海关区'),
    Location(name='承德避暑山庄', address='河北,承德,双桥区'),
    Location(name='沧州铁狮子', address='河北,沧州,新华区'),
    Location(name='廊坊大运河文化带', address='河北,廊坊,广阳区'),
    Location(name='雄安新区', address='河北,雄安,雄安新区'),
    Location(name='保定古莲花池', address='河北,保定,莲池区'),
    Location(name='张家口崇礼', address='河北,张家口,崇礼区'),
    Location(name='北京环球影城', address='北京,北京,怀柔区'),
    Location(name='北京园博园', address='北京,北京,丰台区'),
    Location(name='白求恩医院', address='北京,北京,朝阳区'),
    Location(name='天津之眼', address='天津,天津,和平区'),
    Location(name='津门故里', address='天津,天津,南开区'),
    Location(name='意式风情区', address='天津,天津,和平区'),
    Location(name='蓟州九山顶', address='天津,天津,蓟州区'),
    Location(name='天津博物馆', address='天津,天津,和平区'),
    Location(name='天津海河', address='天津,天津,河西区'),
    Location(name='古文化街', address='天津,天津,南开区'),
    Location(name='天津滨海新区', address='天津,天津,滨海新区'),
    Location(name='南开大学', address='天津,天津,南开区'),
    Location(name='天津西青', address='天津,天津,西青区'),
    Location(name='塘沽港', address='天津,天津,塘沽区'),
    Location(name='武清大观园', address='天津,天津,武清区'),
    Location(name='静海白鹭湖', address='天津,天津,静海区'),
    Location(name='河北水上公园', address='天津,天津,河北区'),
    Location(name='燕郊', address='河北,廊坊,燕郊'),
    Location(name='天津东丽湖', address='天津,天津,东丽区'),
    Location(name='八达岭长城', address='北京,北京,延庆区'),
    Location(name='密云水库', address='北京,北京,密云区'),
    Location(name='盘古大观', address='北京,北京,朝阳区'),
    Location(name='星光影视园', address='北京,北京,怀柔区'),
    Location(name='北京滑雪场', address='北京,北京,怀柔区'),
    Location(name='北京大兴国际机场', address='北京,北京,大兴区'),
    Location(name='北戴河', address='河北,秦皇岛,北戴河区'),
    Location(name='华北电力大学', address='河北,保定,南市区'),
    Location(name='秦皇岛海洋公园', address='河北,秦皇岛,海港区'),
    Location(name='白求恩医学院', address='河北,唐山,路北区'),
    Location(name='张家口草原天路', address='河北,张家口,怀来县'),
    Location(name='承德小布达拉宫', address='河北,承德,双桥区'),
    Location(name='唐山陶瓷博物馆', address='河北,唐山,路北区'),
    Location(name='邯郸广府古城', address='河北,邯郸,广府区'),
    Location(name='涿州佛教文化园', address='河北,保定,涿州市'),
    Location(name='蓟县盘山', address='天津,天津,蓟州区'),
    Location(name='白洋淀', address='河北,保定,安新县'),
    Location(name='涿州影视城', address='河北,保定,涿州市'),
    Location(name='承德金山岭长城', address='河北,承德,丰宁满族自治县'),
    Location(name='天津泰达国际体育中心', address='天津,天津,滨海新区'),
    Location(name='武清泉水湾', address='天津,天津,武清区'),
    Location(name='北京798艺术区', address='北京,北京,朝阳区'),
    Location(name='北京自然博物馆', address='北京,北京,西城区'),
    Location(name='北京中华世纪坛', address='北京,北京,海淀区'),
    Location(name='八达岭野生动物园', address='北京,北京,延庆区'),
    Location(name='河北省博物馆', address='河北,石家庄,桥东区'),
    Location(name='衡水湖', address='河北,衡水,桃城区'),
    Location(name='华北电力大学', address='河北,保定,南市区'),
    Location(name='京津冀协同发展示范区', address='河北,廊坊,广阳区'),
    Location(name='大兴安岭', address='黑龙江,大兴安岭,大兴安岭地区'),
    Location(name='大厂回族自治县', address='河北,廊坊,大厂'),
    Location(name='哈尔滨中央大街', address='黑龙江,哈尔滨,道里区'),
    Location(name='索非亚教堂', address='黑龙江,哈尔滨,道里区'),
    Location(name='冰雪大世界', address='黑龙江,哈尔滨,松北区'),
    Location(name='哈尔滨国际冰雪节', address='黑龙江,哈尔滨,松北区'),
    Location(name='黑龙江省博物馆', address='黑龙江,哈尔滨,南岗区'),
    Location(name='大庆油田', address='黑龙江,大庆,萨尔图区'),
    Location(name='五大连池', address='黑龙江,大庆,五大连池市'),
    Location(name='漠河北极村', address='黑龙江,大兴安岭,漠河'),
    Location(name='齐齐哈尔扎龙湿地', address='黑龙江,齐齐哈尔,扎龙'),
    Location(name='哈尔滨极地馆', address='黑龙江,哈尔滨,南岗区'),
    Location(name='龙江大厦', address='黑龙江,哈尔滨,南岗区'),
    Location(name='大庆红岗', address='黑龙江,大庆,红岗区'),
    Location(name='双鸭山矿山公园', address='黑龙江,双鸭山,双鸭山区'),
    Location(name='佳木斯东极', address='黑龙江,佳木斯,桦川县'),
    Location(name='鸡西矿山公园', address='黑龙江,鸡西,鸡冠区'),
    Location(name='牡丹江镜泊湖', address='黑龙江,牡丹江,东宁县'),
    Location(name='抚远黑瞎子岛', address='黑龙江,抚远,黑瞎子岛'),
    Location(name='松花江', address='黑龙江,哈尔滨,道外区'),
    Location(name='沈阳故宫', address='辽宁,沈阳,沈河区'),
    Location(name='张氏帅府', address='辽宁,沈阳,沈河区'),
    Location(name='九一八历史博物馆', address='辽宁,沈阳,和平区'),
    Location(name='沈阳北陵公园', address='辽宁,沈阳,皇姑区'),
    Location(name='抚顺雷锋纪念馆', address='辽宁,抚顺,顺城区'),
    Location(name='本溪水洞', address='辽宁,本溪,本溪满族自治县'),
    Location(name='营口西市古玩城', address='辽宁,营口,西市区'),
    Location(name='丹东鸭绿江', address='辽宁,丹东,元宝区'),
    Location(name='鞍山千山风景区', address='辽宁,鞍山,千山区'),
    Location(name='辽阳白塔', address='辽宁,辽阳,白塔区'),
    Location(name='锦州古文化街', address='辽宁,锦州,凌河区'),
    Location(name='铁岭白塔', address='辽宁,铁岭,银州区'),
    Location(name='盘锦红海滩', address='辽宁,盘锦,盘山'),
    Location(name='葫芦岛南台', address='辽宁,葫芦岛,南票区'),
    Location(name='长春伪满皇宫', address='吉林,长春,南关区'),
    Location(name='长春博物馆', address='吉林,长春,朝阳区'),
    Location(name='净月潭国家森林公园', address='吉林,长春,二道区'),
    Location(name='吉林松花湖', address='吉林,吉林,船营区'),
    Location(name='延边朝鲜族自治州', address='吉林,延边,延吉市'),
    Location(name='吉林省博物院', address='吉林,吉林,南关区'),
    Location(name='长春电影制片厂', address='吉林,长春,朝阳区'),
    Location(name='白山松水', address='吉林,白山,八道江区'),
    Location(name='图们江', address='吉林,延边,图们'),
    Location(name='松原查干湖', address='吉林,松原,查干湖'),
    Location(name='辽源白山', address='吉林,辽源,辽源区'),
    Location(name='集安古城', address='吉林,通化,集安'),
    Location(name='四平抗联纪念馆', address='吉林,四平,铁东区'),
    Location(name='通化梅河口', address='吉林,通化,梅河口市'),
    Location(name='长白山', address='吉林,白山,长白山'),
    Location(name='黑龙江省博物馆', address='黑龙江,哈尔滨,南岗区'),
    Location(name='海林市', address='黑龙江,牡丹江,海林市'),
    Location(name='牡丹江东极村', address='黑龙江,牡丹江,东极村'),
    Location(name='扎龙自然保护区', address='黑龙江,齐齐哈尔,扎龙'),
    Location(name='双鸭山博物馆', address='黑龙江,双鸭山,双鸭山区'),
    Location(name='黑河湿地', address='黑龙江,黑河,黑河市'),
    Location(name='沈阳中街', address='辽宁,沈阳,和平区'),
    Location(name='葫芦岛龙湾', address='辽宁,葫芦岛,龙港区'),
    Location(name='抚顺水洞', address='辽宁,抚顺,新抚区'),
    Location(name='盘锦红海滩', address='辽宁,盘锦,盘山'),
    Location(name='白山城', address='吉林,白山,八道江区'),
    Location(name='铁岭银州', address='辽宁,铁岭,银州区'),
    Location(name='长春冰雪大世界', address='吉林,长春,朝阳区'),
    Location(name='辽宁省博物馆', address='辽宁,沈阳,和平区'),
    Location(name='黑龙江大庆', address='黑龙江,大庆,萨尔图区'),
    Location(name='吉林大学', address='吉林,长春,朝阳区'),
    Location(name='丹东鸭绿江', address='辽宁,丹东,元宝区'),
    Location(name='本溪水洞', address='辽宁,本溪,本溪满族自治县'),
    Location(name='长春宽城', address='吉林,长春,宽城区'),
    Location(name='吉林市松花江', address='吉林,吉林,昌邑区'),
    Location(name='岳阳楼', address='湖南,岳阳,岳阳楼区'),
    Location(name='张家界国家森林公园', address='湖南,张家界,武陵源区'),
    Location(name='橘子洲头', address='湖南,长沙,岳麓区'),
    Location(name='长沙博物馆', address='湖南,长沙,芙蓉区'),
    Location(name='韶山毛泽东故居', address='湖南,湘潭,韶山区'),
    Location(name='长沙黄兴步行街', address='湖南,长沙,芙蓉区'),
    Location(name='岳阳楼', address='湖南,岳阳,岳阳楼区'),
    Location(name='湘江风光带', address='湖南,长沙,天心区'),
    Location(name='岳阳八百里洞庭湖', address='湖南,岳阳,岳阳楼区'),
    Location(name='长沙大围山', address='湖南,长沙,宁乡市'),
    Location(name='株洲神农城', address='湖南,株洲,天元区'),
    Location(name='长沙博物馆', address='湖南,长沙,芙蓉区'),
    Location(name='常德桃花源', address='湖南,常德,桃源区'),
    Location(name='益阳桃花源', address='湖南,益阳,桃江县'),
    Location(name='湘西凤凰古城', address='湖南,湘西,凤凰县'),
    Location(name='长沙长沙县', address='湖南,长沙,长沙县'),
    Location(name='邵阳武冈', address='湖南,邵阳,武冈市'),
    Location(name='岳阳南湖', address='湖南,岳阳,岳阳楼区'),
    Location(name='黄冈黄梅', address='湖北,黄冈,黄梅县'),
    Location(name='武汉黄鹤楼', address='湖北,武汉,武昌区'),
    Location(name='武汉大学', address='湖北,武汉,武昌区'),
    Location(name='武汉博物馆', address='湖北,武汉,洪山区'),
    Location(name='武汉园博园', address='湖北,武汉,汉阳区'),
    Location(name='鄂州梁子湖', address='湖北,鄂州,梁子湖区'),
    Location(name='荆州古城', address='湖北,荆州,荆州区'),
    Location(name='宜昌三峡大坝', address='湖北,宜昌,夷陵区'),
    Location(name='襄阳古隆中', address='湖北,襄阳,襄城区'),
    Location(name='恩施大峡谷', address='湖北,恩施,恩施市'),
    Location(name='咸宁温泉', address='湖北,咸宁,咸安区'),
    Location(name='黄石东湖', address='湖北,黄石,黄石港区'),
    Location(name='天门小镇', address='湖北,天门,天门市'),
    Location(name='武汉光谷', address='湖北,武汉,洪山区'),
    Location(name='荆门东宝', address='湖北,荆门,东宝区'),
    Location(name='随州大洪山', address='湖北,随州,随州区'),
    Location(name='神农架林区', address='湖北,神农架,神农架林区'),
    Location(name='武汉汉口里', address='湖北,武汉,江汉区'),
    Location(name='十堰丹江口', address='湖北,十堰,丹江口市'),
    Location(name='荆州博物馆', address='湖北,荆州,荆州区'),
    Location(name='黄冈红安', address='湖北,黄冈,红安县'),
    Location(name='武汉江汉路步行街', address='湖北,武汉,江汉区'),
    Location(name='南湖风景区', address='湖北,武汉,洪山区'),
    Location(name='岳阳临湘', address='湖南,岳阳,临湘市'),
    Location(name='长沙星沙', address='湖南,长沙,星沙区'),
    Location(name='株洲醴陵', address='湖南,株洲,醴陵市'),
    Location(name='常德沅江', address='湖南,常德,沅江市'),
    Location(name='岳阳君山', address='湖南,岳阳,君山区'),
    Location(name='湘潭湘江', address='湖南,湘潭,湘江新区'),
    Location(name='郴州东江湖', address='湖南,郴州,桂阳县'),
    Location(name='武汉天河机场', address='湖北,武汉,黄陂区'),
    Location(name='武汉长江大桥', address='湖北,武汉,汉阳区'),
    Location(name='黄冈大别山', address='湖北,黄冈,黄冈市'),
    Location(name='武汉梅园', address='湖北,武汉,黄陂区'),
    Location(name='岳阳鹤龙湖', address='湖南,岳阳,岳阳楼区'),
    Location(name='娄底双峰', address='湖南,娄底,双峰县'),
    Location(name='湘西土家族苗族自治州', address='湖南,湘西,湘西'),
    Location(name='武汉流行音乐街', address='湖北,武汉,江汉区'),
    Location(name='武汉汉口', address='湖北,武汉,江汉区'),
    Location(name='黄石大冶', address='湖北,黄石,大冶市'),
    Location(name='仙桃天鹅湖', address='湖北,仙桃,仙桃市'),
    Location(name='武穴', address='湖北,黄冈,武穴市'),
    Location(name='随州随县', address='湖北,随州,随县'),
    Location(name='武汉南湖', address='湖北,武汉,洪山区'),
    Location(name='岳阳江河', address='湖南,岳阳,岳阳楼区'),
    Location(name='长沙明德', address='湖南,长沙,天心区'),
    Location(name='武汉花博汇', address='湖北,武汉,江夏区'),
    Location(name='恩施白云山', address='湖北,恩施,恩施市'),
    Location(name='长阳土家族自治县', address='湖北,宜昌,长阳土家族自治县'),
    Location(name='仙桃沙湖', address='湖北,仙桃,仙桃市'),
    Location(name='常德市博物馆', address='湖南,常德,武陵区'),
    Location(name='湘潭湘江新区', address='湖南,湘潭,湘江新区'),
    Location(name='湖北省博物馆', address='湖北,武汉,武昌区'),
    Location(name='长沙白鹤', address='湖南,长沙,长沙县'),
    Location(name='桂林漓江', address='广西,桂林,象山区'),
    Location(name='阳朔西街', address='广西,桂林,阳朔县'),
    Location(name='南宁青秀山', address='广西,南宁,青秀区'),
    Location(name='北海银滩', address='广西,北海,银海区'),
    Location(name='防城港东兴', address='广西,防城港,东兴市'),
    Location(name='百色靖西', address='广西,百色,靖西市'),
    Location(name='桂林象鼻山', address='广西,桂林,象山区'),
    Location(name='南宁人民公园', address='广西,南宁,兴宁区'),
    Location(name='崇左友谊关', address='广西,崇左,友谊关'),
    Location(name='柳州龙城', address='广西,柳州,柳北区'),
    Location(name='贺州八步', address='广西,贺州,八步区'),
    Location(name='桂平西山', address='广西,桂平,西山镇'),
    Location(name='龙胜梯田', address='广西,桂林,龙胜各族自治县'),
    Location(name='南宁大明山', address='广西,南宁,马山县'),
    Location(name='合浦汉墓', address='广西,合浦,合浦县'),
    Location(name='钦州钦州港', address='广西,钦州,钦南区'),
    Location(name='玉林博白', address='广西,玉林,博白县'),
    Location(name='南宁中山路步行街', address='广西,南宁,青秀区'),
    Location(name='桂林两江四湖', address='广西,桂林,叠彩区'),
    Location(name='梧州龙圩', address='广西,梧州,龙圩区'),
    Location(name='广州塔', address='广东,广州,海珠区'),
    Location(name='白云山', address='广东,广州,白云区'),
    Location(name='深圳大梅沙', address='广东,深圳,盐田区'),
    Location(name='珠海长隆海洋王国', address='广东,珠海,横琴新区'),
    Location(name='佛山祖庙', address='广东,佛山,禅城区'),
    Location(name='东莞樟木头', address='广东,东莞,樟木头镇'),
    Location(name='中山孙中山故居', address='广东,中山,翠亨村'),
    Location(name='韶关丹霞山', address='广东,韶关,武江区'),
    Location(name='江门开平碉楼', address='广东,江门,开平市'),
    Location(name='惠州西湖', address='广东,惠州,惠城区'),
    Location(name='阳江海陵岛', address='广东,阳江,阳春市'),
    Location(name='梅州客天下', address='广东,梅州,梅县区'),
    Location(name='清远英西峰林', address='广东,清远,英德市'),
    Location(name='肇庆星湖', address='广东,肇庆,端州区'),
    Location(name='广州上下九步行街', address='广东,广州,荔湾区'),
    Location(name='深圳华侨城', address='广东,深圳,南山区'),
    Location(name='广州长隆野生动物世界', address='广东,广州,番禺区'),
    Location(name='汕头小公园', address='广东,汕头,金平区'),
    Location(name='河源万绿湖', address='广东,河源,源城区'),
    Location(name='茂名浪漫海岸', address='广东,茂名,电白区'),
    Location(name='珠海情侣路', address='广东,珠海,香洲区'),
    Location(name='深圳华强北', address='广东,深圳,福田区'),
    Location(name='韶关南华寺', address='广东,韶关,曲江区'),
    Location(name='广州市博物馆', address='广东,广州,越秀区'),
    Location(name='湛江南三岛', address='广东,湛江,赤坎区'),
    Location(name='清远白石山', address='广东,清远,清城区'),
    Location(name='汕尾红海湾', address='广东,汕尾,红海湾'),
    Location(name='东莞南城', address='广东,东莞,南城区'),
    Location(name='广州越秀公园', address='广东,广州,越秀区'),
    Location(name='南宁南湖公园', address='广西,南宁,青秀区'),
    Location(name='桂林德天瀑布', address='广西,崇左,德天乡'),
    Location(name='北海老街', address='广西,北海,海城区'),
    Location(name='柳州柳江', address='广西,柳州,城中区'),
    Location(name='南宁东盟博览会', address='广西,南宁,青秀区'),
    Location(name='贺州黄姚古镇', address='广西,贺州,昭平县'),
    Location(name='桂林阳朔', address='广西,桂林,阳朔县'),
    Location(name='钦州灵山大佛', address='广西,钦州,钦北区'),
    Location(name='防城港海洋公园', address='广西,防城港,港口区'),
    Location(name='南宁博物馆', address='广西,南宁,青秀区'),
    Location(name='南宁西乡塘', address='广西,南宁,西乡塘区'),
    Location(name='广西民族博物馆', address='广西,南宁,青秀区'),
    Location(name='桂林龙脊梯田', address='广西,桂林,龙胜各族自治县'),
    Location(name='广州白云国际机场', address='广东,广州,白云区'),
    Location(name='珠海博物馆', address='广东,珠海,香洲区'),
    Location(name='佛山南风古灶', address='广东,佛山,南海区'),
    Location(name='东莞可园', address='广东,东莞,东莞市'),
    Location(name='韶关小北江', address='广东,韶关,浈江区'),
    Location(name='肇庆七星岩', address='广东,肇庆,端州区'),
    Location(name='河源博物馆', address='广东,河源,源城区'),
    Location(name='阳江海陵岛', address='广东,阳江,阳春市'),
    Location(name='广州农博园', address='广东,广州,花都区'),
    Location(name='清远清新', address='广东,清远,清新区'),
    Location(name='深圳福田CBD', address='广东,深圳,福田区'),
    Location(name='惠州红花湖', address='广东,惠州,惠阳区'),
    Location(name='汕头老市区', address='广东,汕头,金平区'),
    Location(name='茂名博物馆', address='广东,茂名,茂南区'),
    Location(name='广州白云山', address='广东,广州,白云区'),
    Location(name='维多利亚港', address='香港,香港岛,中西区'),
    Location(name='香港迪士尼乐园', address='香港,香港,大屿山'),
    Location(name='太平山顶', address='香港,香港岛,中西区'),
    Location(name='星光大道', address='香港,九龙,尖沙咀'),
    Location(name='天坛大佛', address='香港,大屿山,梅窝'),
    Location(name='海洋公园', address='香港,香港岛,南区'),
    Location(name='香港历史博物馆', address='香港,九龙,尖沙咀'),
    Location(name='旺角街市', address='香港,九龙,旺角'),
    Location(name='香港文化博物馆', address='香港,九龙,沙田区'),
    Location(name='香港博物馆', address='香港,九龙,九龙城区'),
    Location(name='赤柱市场', address='香港,香港岛,南区'),
    Location(name='尖沙咀天星码头', address='香港,九龙,尖沙咀'),
    Location(name='香港科学馆', address='香港,九龙,尖沙咀'),
    Location(name='香港动植物公园', address='香港,香港岛,中西区'),
    Location(name='铜锣湾购物区', address='香港,香港岛,东区'),
    Location(name='澳门威尼斯人度假村', address='澳门,澳门,路氹城'),
    Location(name='大三巴牌坊', address='澳门,澳门,圣方济各堂区'),
    Location(name='澳门塔', address='澳门,澳门,南区'),
    Location(name='澳门博物馆', address='澳门,澳门,花地玛堂区'),
    Location(name='氹仔市中心', address='澳门,澳门,氹仔'),
    Location(name='路环海滩', address='澳门,澳门,路环'),
    Location(name='圣保禄学院遗址', address='澳门,澳门,圣方济各堂区'),
    Location(name='澳门科学馆', address='澳门,澳门,路氹城'),
    Location(name='龙环葡韵', address='澳门,澳门,氹仔'),
    Location(name='香港科技大学', address='香港,香港岛,西贡区'),
    Location(name='香港中文大学', address='香港,香港,沙田区'),
    Location(name='香港城市大学', address='香港,九龙,九龙城'),
    Location(name='台北101', address='台湾,台北,信义区'),
    Location(name='故宫博物院', address='台湾,台北,士林区'),
    Location(name='士林夜市', address='台湾,台北,士林区'),
    Location(name='阳明山国家公园', address='台湾,台北,阳明山'),
    Location(name='九份老街', address='台湾,新北,瑞芳区'),
    Location(name='淡水老街', address='台湾,新北,淡水区'),
    Location(name='基隆港', address='台湾,基隆,仁爱区'),
    Location(name='阿里山国家风景区', address='台湾,嘉义,阿里山'),
    Location(name='日月潭', address='台湾,南投,鱼池乡'),
    Location(name='花莲太鲁阁', address='台湾,花莲,太鲁阁'),
    Location(name='垦丁国家公园', address='台湾,屏东,垦丁'),
    Location(name='屏东牡丹湾', address='台湾,屏东,牡丹乡'),
    Location(name='桃园大溪', address='台湾,桃园,大溪镇'),
    Location(name='台中逢甲夜市', address='台湾,台中,西屯区'),
    Location(name='嘉义文化创意产业园区', address='台湾,嘉义,东区'),
    Location(name='宜兰罗东夜市', address='台湾,宜兰,罗东镇'),
    Location(name='新竹县东门市场', address='台湾,新竹,东区'),
    Location(name='高雄蓮池潭', address='台湾,高雄,左营区'),
    Location(name='南投埔里镇', address='台湾,南投,埔里镇'),
    Location(name='花莲七星潭', address='台湾,花莲,花莲市'),
    Location(name='苗栗通霄镇', address='台湾,苗栗,通霄镇'),
    Location(name='彰化鹿港镇', address='台湾,彰化,鹿港镇'),
    Location(name='高雄草衙飞行器博物馆', address='台湾,高雄,凤山'),
    Location(name='台北士林官邸', address='台湾,台北,士林区'),
    Location(name='基隆庙口夜市', address='台湾,基隆,中正区'),
    Location(name='台南安平古堡', address='台湾,台南,安平区'),
    Location(name='屏东小琉球', address='台湾,屏东,琉球乡'),
    Location(name='澎湖列岛', address='台湾,澎湖,澎湖县'),
    Location(name='金门列岛', address='台湾,金门,金门县'),
    Location(name='马祖列岛', address='台湾,连江,马祖'),
    Location(name='台北松山文创园区', address='台湾,台北,松山区'),
    Location(name='南投草屯', address='台湾,南投,草屯镇'),
    Location(name='台南孔庙', address='台湾,台南,中西区'),
    Location(name='台北华山1914文创园区', address='台湾,台北,中正区'),
    Location(name='高雄六合夜市', address='台湾,高雄,苓雅区'),
    Location(name='宜兰三星葱', address='台湾,宜兰,三星乡'),
    Location(name='台中高美湿地', address='台湾,台中,大肚区'),
    Location(name='彰化扇形车站', address='台湾,彰化,彰化市'),
    Location(name='新北三峡老街', address='台湾,新北,三峡区'),
    Location(name='桃园龟山', address='台湾,桃园,龟山'),
    Location(name='高雄旗津', address='台湾,高雄,旗津区'),
    Location(name='桃园航空城', address='台湾,桃园,桃园市'),
    Location(name='花莲鲤鱼潭', address='台湾,花莲,花莲市'),
    Location(name='南投水里蛇窯', address='台湾,南投,水里乡'),
     Location(name='西安钟楼', address='陕西,西安,碑林区'),
    Location(name='兵马俑', address='陕西,西安,临潼区'),
    Location(name='华清池', address='陕西,西安,临潼区'),
    Location(name='大雁塔', address='陕西,西安,雁塔区'),
    Location(name='西安城墙', address='陕西,西安,碑林区'),
    Location(name='小雁塔', address='陕西,西安,碑林区'),
    Location(name='曲江池遗址公园', address='陕西,西安,曲江新区'),
    Location(name='陕西历史博物馆', address='陕西,西安,碑林区'),
    Location(name='西安博物馆', address='陕西,西安,碑林区'),
    Location(name='钟鼓楼', address='陕西,西安,莲湖区'),
    Location(name='华山', address='陕西,华阴,华山'),
    Location(name='延安革命纪念馆', address='陕西,延安,宝塔区'),
    Location(name='延安枣园', address='陕西,延安,延安新区'),
    Location(name='榆林古城', address='陕西,榆林,榆阳区'),
    Location(name='秦始皇陵', address='陕西,西安,临潼区'),
    Location(name='神木红碱淖', address='陕西,神木,红碱淖'),
    Location(name='宝鸡青铜器博物馆', address='陕西,宝鸡,金台区'),
    Location(name='甘肃敦煌莫高窟', address='甘肃,敦煌,敦煌市'),
    Location(name='嘉峪关长城', address='甘肃,嘉峪关,嘉峪关市'),
    Location(name='兰州黄河风情线', address='甘肃,兰州,城关区'),
    Location(name='兰州大学', address='甘肃,兰州,城关区'),
    Location(name='天水麦积山', address='甘肃,天水,麦积区'),
    Location(name='平凉崆峒山', address='甘肃,平凉,崆峒区'),
    Location(name='甘南夏河', address='甘肃,甘南,夏河县'),
    Location(name='宁夏沙湖', address='宁夏,银川,灵武市'),
    Location(name='银川贺兰山', address='宁夏,银川,贺兰县'),
    Location(name='银川镇北堡西部影城', address='宁夏,银川,贺兰县'),
    Location(name='中卫沙坡头', address='宁夏,中卫,沙坡头区'),
    Location(name='固原原州区', address='宁夏,固原,原州区'),
    Location(name='青海湖', address='青海,海南州,共和县'),
    Location(name='西宁塔尔寺', address='青海,西宁,湟中区'),
    Location(name='茶卡盐湖', address='青海,海西,乌兰县'),
    Location(name='可可西里', address='青海,海西,可可西里'),
    Location(name='青海湖国家级自然保护区', address='青海,海北,门源县'),
    Location(name='新疆天池', address='新疆,昌吉,阜康市'),
    Location(name='乌鲁木齐红山', address='新疆,乌鲁木齐,天山区'),
    Location(name='喀纳斯湖', address='新疆,阿勒泰,布尔津县'),
    Location(name='吐鲁番火焰山', address='新疆,吐鲁番,吐鲁番市'),
    Location(name='和田玉器', address='新疆,和田,和田市'),
    Location(name='哈密瓜', address='新疆,哈密,哈密市'),
    Location(name='阿尔泰山', address='新疆,阿勒泰,阿勒泰市'),
    Location(name='塔城大草原', address='新疆,塔城,塔城市'),
    Location(name='巴音布鲁克', address='新疆,巴音郭楞,和静县'),
    Location(name='博尔塔拉草原', address='新疆,博尔塔拉,博乐市'),
    Location(name='库尔勒香梨', address='新疆,巴音郭楞,库尔勒市'),
    Location(name='石河子兵团', address='新疆,石河子,石河子市'),
    Location(name='克拉玛依石油博物馆', address='新疆,克拉玛依,克拉玛依市'),
    Location(name='新疆维吾尔自治区博物馆', address='新疆,乌鲁木齐,天山区'),
    Location(name='南疆丝绸之路', address='新疆,喀什,喀什市'),
    Location(name='北疆草原', address='新疆,伊犁,伊宁市'),
    Location(name='新疆吐鲁番地区', address='新疆,吐鲁番,吐鲁番市'),
    Location(name='霍尔果斯口岸', address='新疆,伊犁,霍尔果斯市'),
    Location(name='乌鲁木齐博物馆', address='新疆,乌鲁木齐,新市区'),
    Location(name='甘肃西峰', address='甘肃,平凉,西峰区'),
    Location(name='新疆温泉', address='新疆,昌吉,呼图壁县'),
    Location(name='白河峡谷', address='甘肃,定西,临洮县'),
    Location(name='甘肃张掖丹霞', address='甘肃,张掖,甘州区'),
    Location(name='秦安桃花源', address='甘肃,天水,秦安县'),
    Location(name='新疆天山雪莲', address='新疆,昌吉,玛纳斯县'),
    Location(name='西安大唐不夜城', address='陕西,西安,雁塔区'),
    Location(name='宁夏水洞沟', address='宁夏,银川,银川市'),
    Location(name='青海茶卡盐湖', address='青海,海西,乌兰县'),
    Location(name='甘肃白银', address='甘肃,白银,白银区'),
    Location(name='新疆喀什老城', address='新疆,喀什,喀什市'),
    Location(name='青海湖环湖', address='青海,海北,刚察县'),
    Location(name='青海湖鸟岛', address='青海,海南,共和县'),
    Location(name='西安碑林博物馆', address='陕西,西安,碑林区'),
    Location(name='西安钟鼓楼', address='陕西,西安,莲湖区'),
    Location(name='甘肃武山', address='甘肃,天水,武山县'),
    Location(name='西安北院门美食街', address='陕西,西安,莲湖区'),
    Location(name='甘肃兰州拉面', address='甘肃,兰州,城关区'),
    Location(name='西安南门', address='陕西,西安,碑林区'),
    Location(name='西安西安碑林', address='陕西,西安,碑林区'),
    Location(name='青海坎布拉', address='青海,玉树,囊谦县'),
    Location(name='西安回民街', address='陕西,西安,莲湖区'),
    Location(name='西安大唐西市', address='陕西,西安,莲湖区'),
    Location(name='甘肃景泰蓝', address='甘肃,白银,景泰县'),
    Location(name='青海大通', address='青海,西宁,大通县'),
    Location(name='青海冷湖', address='青海,海西,冷湖镇'),
    Location(name='甘肃金昌', address='甘肃,金昌,金川区'),
    Location(name='阿克苏桃子', address='新疆,阿克苏,阿克苏市'),
    Location(name='乌鲁木齐新疆国际大巴扎', address='新疆,乌鲁木齐,天山区'),
    Location(name='青海门源', address='青海,海北,门源县'),
    Location(name='新疆巴音布鲁克草原', address='新疆,巴音郭楞,和静县'),
    Location(name='西安饭庄', address='陕西,西安,莲湖区'),
    Location(name='青海黄河源', address='青海,果洛,玛沁县'),
    Location(name='新疆喀什噶尔', address='新疆,喀什,喀什市'),
    Location(name='青海德令哈', address='青海,海西,德令哈市'),
    Location(name='西安西安事变纪念馆', address='陕西,西安,碑林区'),
    Location(name='成都大熊猫繁育研究基地', address='四川,成都,成华区'),
    Location(name='青羊宫', address='四川,成都,青羊区'),
    Location(name='武侯祠', address='四川,成都,武侯区'),
    Location(name='宽窄巷子', address='四川,成都,青羊区'),
    Location(name='锦里古街', address='四川,成都,武侯区'),
    Location(name='乐山大佛', address='四川,乐山,市中区'),
    Location(name='峨眉山', address='四川,乐山,峨眉山市'),
    Location(name='都江堰', address='四川,成都,都江堰市'),
    Location(name='稻城亚丁', address='四川,甘孜,稻城县'),
    Location(name='九寨沟', address='四川,阿坝,九寨沟县'),
    Location(name='黄龙', address='四川,阿坝,松潘县'),
    Location(name='绵阳科学城', address='四川,绵阳,游仙区'),
    Location(name='南充阆中古城', address='四川,南充,阆中市'),
    Location(name='重庆洪崖洞', address='重庆,重庆,渝中区'),
    Location(name='解放碑', address='重庆,重庆,渝中区'),
    Location(name='磁器口古镇', address='重庆,重庆,沙坪坝区'),
    Location(name='大足石刻', address='重庆,大足,大足区'),
    Location(name='武隆喀斯特', address='重庆,重庆,武隆区'),
    Location(name='重庆夜景', address='重庆,重庆,渝中区'),
    Location(name='云南石林', address='云南,昆明,石林县'),
    Location(name='丽江古城', address='云南,丽江,丽江古城'),
    Location(name='大理洱海', address='云南,大理,大理市'),
    Location(name='香格里拉', address='云南,迪庆,香格里拉市'),
    Location(name='昆明滇池', address='云南,昆明,滇池'),
    Location(name='玉龙雪山', address='云南,丽江,玉龙纳西族自治县'),
    Location(name='泸沽湖', address='云南,丽江,宁蒗彝族自治县'),
    Location(name='元阳梯田', address='云南,红河,元阳县'),
    Location(name='西双版纳热带植物园', address='云南,西双版纳,勐腊县'),
    Location(name='贵州黄果树瀑布', address='贵州,安顺,镇宁布依族苗族自治县'),
    Location(name='贵阳甲秀楼', address='贵州,贵阳,南明区'),
    Location(name='荔波小七孔', address='贵州,黔南,荔波县'),
    Location(name='贵州苗寨', address='贵州,黔东南,凯里市'),
    Location(name='毕节织金洞', address='贵州,毕节,织金县'),
    Location(name='黔灵山公园', address='贵州,贵阳,云岩区'),
    Location(name='西藏布达拉宫', address='西藏,拉萨,城关区'),
    Location(name='纳木错', address='西藏,那曲,那曲县'),
    Location(name='珠峰大本营', address='西藏,定日,珠穆朗玛峰'),
    Location(name='林芝桃花', address='西藏,林芝,林芝市'),
    Location(name='西藏博物馆', address='西藏,拉萨,城关区'),
    Location(name='羊卓雍湖', address='西藏,山南,羊卓雍湖'),
    Location(name='亚丁风景区', address='四川,甘孜,稻城县'),
    Location(name='九寨沟风景名胜区', address='四川,阿坝,九寨沟县'),
    Location(name='乐山大佛景区', address='四川,乐山,乐山市'),
    Location(name='绵阳涪城区', address='四川,绵阳,涪城区'),
    Location(name='南充市阆中古城', address='四川,南充,阆中市'),
    Location(name='重庆长江索道', address='重庆,重庆,渝中区'),
    Location(name='九华山', address='四川,绵阳,九华山'),
    Location(name='自贡灯会', address='四川,自贡,自流井区'),
    Location(name='大理古城', address='云南,大理,大理市'),
    Location(name='云南世博园', address='云南,昆明,官渡区'),
    Location(name='普洱茶山', address='云南,普洱,宁洱县'),
    Location(name='泸沽湖环湖', address='云南,丽江,宁蒗彝族自治县'),
    Location(name='昆明大观公园', address='云南,昆明,盘龙区'),
    Location(name='贵阳风景名胜区', address='贵州,贵阳,南明区'),
    Location(name='贵阳观山湖', address='贵州,贵阳,观山湖区'),
    Location(name='四川宜宾竹海', address='四川,宜宾,竹海'),
    Location(name='贵阳百花山', address='贵州,贵阳,花溪区'),
    Location(name='阿坝藏族羌族自治州', address='四川,阿坝,阿坝县'),
    Location(name='大理古城夜景', address='云南,大理,大理市'),
    Location(name='丽江千古情', address='云南,丽江,丽江古城'),
    Location(name='德阳黄河大峡谷', address='四川,德阳,广汉市'),
    Location(name='宜宾蜀南竹海', address='四川,宜宾,宜宾县'),
    Location(name='泸州老窖', address='四川,泸州,龙马潭区'),
    Location(name='重庆两江夜景', address='重庆,重庆,渝中区'),
    Location(name='安顺黄果树', address='贵州,安顺,镇宁布依族苗族自治县'),
    Location(name='贵阳红枫湖', address='贵州,贵阳,开阳县'),
    Location(name='丽江纳西文化', address='云南,丽江,丽江古城'),
    Location(name='成都春熙路', address='四川,成都,锦江区'),
    Location(name='成都杜甫草堂', address='四川,成都,青羊区'),
    Location(name='云南昆明滇池', address='云南,昆明,滇池'),
    Location(name='西安南门', address='陕西,西安,碑林区'),
    Location(name='西安西安碑林', address='陕西,西安,碑林区'),
    Location(name='黔东南苗族侗族自治州', address='贵州,黔东南,凯里市'),
    Location(name='四川青城山', address='四川,都江堰,青城山'),
    Location(name='贵阳雷公山', address='贵州,贵阳,花溪区'),
    Location(name='四川雅安熊猫基地', address='四川,雅安,雨城区'),
    Location(name='云南大理白族自治州', address='云南,大理,大理市'),
    Location(name='西藏拉萨', address='西藏,拉萨,城关区'),
    Location(name='西藏纳木错', address='西藏,那曲,那曲县'),
    Location(name='重庆武隆', address='重庆,重庆,武隆区'),
    Location(name='贵阳青岩古镇', address='贵州,贵阳,修文县'),
    Location(name='西安小雁塔', address='陕西,西安,碑林区'),
    Location(name='西安博物馆', address='陕西,西安,碑林区'),
    Location(name='重庆长江', address='重庆,重庆,长江'),
    Location(name='贵州赤水', address='贵州,遵义,赤水市'),
    Location(name='云南昆明石林', address='云南,昆明,石林县'),
    Location(name='四川阿坝藏族羌族自治州', address='四川,阿坝,阿坝县'),
    Location(name='云南滇池', address='云南,昆明,滇池'),
    Location(name='西安大唐不夜城', address='陕西,西安,雁塔区'),
    Location(name='重庆解放碑', address='重庆,重庆,渝中区'),
    Location(name='西藏羊卓雍湖', address='西藏,山南,羊卓雍湖'),
    Location(name='贵州安顺', address='贵州,安顺,安顺市'),
     Location(name='呼伦贝尔大草原', address='内蒙古,呼伦贝尔,海拉尔区'),
    Location(name='阿尔山国家森林公园', address='内蒙古,阿尔山,阿尔山市'),
    Location(name='额济纳旗胡杨林', address='内蒙古,阿拉善,额济纳旗'),
    Location(name='乌兰察布大草原', address='内蒙古,乌兰察布,集宁区'),
    Location(name='锡林郭勒盟草原', address='内蒙古,锡林郭勒,锡林浩特市'),
    Location(name='鄂尔多斯草原', address='内蒙古,鄂尔多斯,鄂尔多斯市'),
    Location(name='包头青山', address='内蒙古,包头,青山区'),
    Location(name='内蒙古博物馆', address='内蒙古,呼和浩特,新城区'),
    Location(name='呼和浩特大昭寺', address='内蒙古,呼和浩特,赛罕区'),
    Location(name='乌兰浩特', address='内蒙古,兴安盟,乌兰浩特市'),
    Location(name='巴彦淖尔黄河', address='内蒙古,巴彦淖尔,临河区'),
    Location(name='扎兰屯', address='内蒙古,呼伦贝尔,扎兰屯市'),
    Location(name='山西平遥古城', address='山西,晋中,平遥县'),
    Location(name='大同云冈石窟', address='山西,大同,云冈区'),
    Location(name='运城盐湖', address='山西,运城,盐湖区'),
    Location(name='太原晋祠', address='山西,太原,晋源区'),
    Location(name='五台山', address='山西,忻州,五台县'),
    Location(name='盂山国家森林公园', address='山西,阳泉,盂县'),
    Location(name='山西博物院', address='山西,太原,小店区'),
    Location(name='晋中灵石县', address='山西,晋中,灵石县'),
    Location(name='临汾壶口瀑布', address='山西,临汾,吉县'),
    Location(name='河南少林寺', address='河南,郑州,登封市'),
    Location(name='龙门石窟', address='河南,洛阳,龙门镇'),
    Location(name='嵩山', address='河南,郑州,登封市'),
    Location(name='开封汴京', address='河南,开封,龙亭区'),
    Location(name='郑州博物馆', address='河南,郑州,金水区'),
    Location(name='河南省人民医院', address='河南,郑州,二七区'),
    Location(name='河南新乡辉县', address='河南,新乡,辉县市'),
    Location(name='焦作云台山', address='河南,焦作,修武县'),
    Location(name='南阳卧龙岗', address='河南,南阳,卧龙区'),
    Location(name='福建武夷山', address='福建,南平,武夷山市'),
    Location(name='泉州古城', address='福建,泉州,鲤城区'),
    Location(name='福州三坊七巷', address='福建,福州,鼓楼区'),
    Location(name='厦门鼓浪屿', address='福建,厦门,思明区'),
    Location(name='泉州南门', address='福建,泉州,丰泽区'),
    Location(name='福建沙县小吃', address='福建,三明,沙县'),
    Location(name='龙岩永定土楼', address='福建,龙岩,永定区'),
    Location(name='福州西湖公园', address='福建,福州,鼓楼区'),
    Location(name='南平建瓯', address='福建,南平,建瓯市'),
    Location(name='济南趵突泉', address='山东,济南,历下区'),
    Location(name='青岛栈桥', address='山东,青岛,市南区'),
    Location(name='泰山', address='山东,泰安,泰山区'),
    Location(name='曲阜孔庙', address='山东,曲阜,曲阜市'),
    Location(name='烟台蓬莱阁', address='山东,烟台,蓬莱区'),
    Location(name='潍坊风筝博物馆', address='山东,潍坊,潍城区'),
    Location(name='威海刘公岛', address='山东,威海,环翠区'),
    Location(name='临沂沂蒙山', address='山东,临沂,沂南县'),
    Location(name='烟台山', address='山东,烟台,芝罘区'),
    Location(name='西藏布达拉宫', address='西藏,拉萨,城关区'),
    Location(name='纳木错', address='西藏,那曲,那曲县'),
    Location(name='西藏大昭寺', address='西藏,拉萨,城关区'),
    Location(name='珠峰大本营', address='西藏,定日,珠穆朗玛峰'),
    Location(name='西藏雅鲁藏布江', address='西藏,林芝,林芝市'),
    Location(name='西藏林芝', address='西藏,林芝,林芝市'),
    Location(name='山南市', address='西藏,山南,山南市'),
    Location(name='昌都地区', address='西藏,昌都,昌都市'),
    Location(name='日喀则', address='西藏,日喀则,日喀则市'),
    Location(name='林芝桃花', address='西藏,林芝,林芝市'),
    Location(name='西安城墙', address='陕西,西安,碑林区'),
    Location(name='太原南山', address='山西,太原,迎泽区'),
    Location(name='黄河壶口瀑布', address='山西,临汾,吉县'),
    Location(name='朔州应县木塔', address='山西,朔州,应县'),
    Location(name='运城盐湖', address='山西,运城,盐湖区'),
    Location(name='临汾红旗渠', address='山西,临汾,红旗渠'),
    Location(name='山西大同', address='山西,大同,大同市'),
    Location(name='西安小雁塔', address='陕西,西安,碑林区'),
    Location(name='临汾侯马', address='山西,临汾,侯马市'),
    Location(name='安阳殷墟', address='河南,安阳,殷都区'),
    Location(name='平顶山云台山', address='河南,平顶山,云台山'),
    Location(name='郑州华山', address='河南,郑州,华山'),
    Location(name='洛阳老城', address='河南,洛阳,老城区'),
    Location(name='信阳鸡公山', address='河南,信阳,鸡公山'),
    Location(name='开封包子', address='河南,开封,包子铺'),
    Location(name='新乡辉县', address='河南,新乡,辉县'),
    Location(name='驻马店', address='河南,驻马店,驿城区'),
    Location(name='莆田湄洲岛', address='福建,莆田,湄洲岛'),
    Location(name='泉州东街口', address='福建,泉州,鲤城区'),
    Location(name='南平建阳', address='福建,南平,建阳区'),
    Location(name='福州西湖', address='福建,福州,鼓楼区'),
    Location(name='厦门白城', address='福建,厦门,思明区'),
    Location(name='漳州南靖', address='福建,漳州,南靖县'),
    Location(name='福州仓山', address='福建,福州,仓山区'),
    Location(name='莆田市秀屿区', address='福建,莆田,秀屿区'),
    Location(name='德州扒鸡', address='山东,德州,德城区'),
    Location(name='青岛海滨', address='山东,青岛,市南区'),
    Location(name='烟台葡萄', address='山东,烟台,莱山区'),
    Location(name='济宁曲阜', address='山东,济宁,曲阜市'),
    Location(name='淄博博山', address='山东,淄博,博山区'),
    Location(name='莱芜', address='山东,莱芜,莱城区'),
    Location(name='聊城东昌湖', address='山东,聊城,东昌府区'),
]


# 执行批量插入
Location.objects.bulk_create(locations)

print("Location地点数据已成功插入！")

