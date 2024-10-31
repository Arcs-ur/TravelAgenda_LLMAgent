# G3
# 配置说明

## 环境变量设置
安装python-decouple 库

	pip install python-decouple
在G3目录下创建 .env 文件

文件内容：

	EMAIL_HOST_PASSWORD = 发件人邮箱密码

## 文件夹内容说明
1. accounts
用户账户管理模块的app
database added
2. agenda
日程管理模板的app
database added
3. dashboard
仪表盘（用户登录进去看到的页面）

4. destinations
旅游景点，酒店，餐厅，购物展示以及交通
database added
5. posts
发帖子模块的app
database added
6. static静态文件
home_assets是初始页面的和旅游推荐系统没关系

7. templates模板
利用模板继承base.html，实现各个子网页的前端开发，路由跳转用django的url模板实现

8. database内容初始化模块
在TravelAgenda文件夹下面加了一个databaseInit文件夹，里面放数据库内容“一键添加”的脚本，运行的时候要切到G3/TravelAgenda下面运行，python3 databaseInit/agenda_location_init.py类似于这样运行