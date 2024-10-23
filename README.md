# G3
# 配置说明
在settings.py中加上
AUTH_USER_MODEL = 'accounts.CustomUser'
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