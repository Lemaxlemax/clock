# clock-in：易班打卡脚本
<br/>
*说明*：由于近期易班让部分网页只能通过腾讯的X5内核才能访问（比如微信），而QQ浏览器的chromium版本低，所以只能用旧版的模块+驱动器模拟，非常麻烦；写代码时还发现3.8版本的selenium在控制ActionChains对象时存在无法避免的错误，似乎只能通过更新解决，所以代码在点击模拟上做了很大的妥协。
<br/>
### 教程
1. 安装QQ浏览器，注意不要给它多余的权限
2. 将chromedriver.exe放置在QQ浏览器文件目录中，即与TencentQQBrowserchrome.exe同级
3. 根据requirements.txt安装库，可以搭建一个虚拟环境
4. 修改mark.py里的手机号和密码变量，运行mark.py
5. 可以把脚本打包成程序在计算机管理中设置定时（800am以后）开启，注意休眠和睡眠的选项
