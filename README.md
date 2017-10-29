# 项目初始化
打开命令行，运行git clone https://github.com/y19941115mx/django下载项目源码
1. cd django 进入项目目录
2. docker-compose up -d 启动服务，第一次运行需要下载镜像，会比较慢，请耐心等候
3. make run  创建数据库，同时生成一个超级管理员，用来登录后台，按照提示输入用户名、密码即可
4. make import 进入mysql数据库
在 mysql命令行中输入
1. use mysite; 选择数据库
2. source /etc/mysql/conf.d/mysqldata; 导入数据,注意后面有；符号不能忘
3. exit 退出数据库程序

# 无法访问
1. 输入 docker-compose restart

# Ubuntu 如果关机 重新启动命令
上述内容重新来一遍

# 查看项目
在Ubuntu虚拟机中访问 http://127.0.0.1:8000/ 就可以看到项目了 啦啦啦！
或者使用ifconfig查询虚拟机的地址+8000 可以在本机看到项目

# 用例
插入日期在2017年10月31日 到2017年11月1日的订单 提示无法插入



