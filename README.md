# linux-awvs-
patch_awvs是破解文件
如何安装与破解的步骤已经公布了,此处放置链接:
此处为网盘下载链接:
二：Linux_awvs安装记录

环境：Ubuntu 16.04.1 LTS

安装好依赖:

sudo apt-get install libxdamage1 libgtk-3-0 libasound2 libnss3 libxss1 -y

官方安装脚本链接：链接：https://pan.baidu.com/s/1EIOyiVR-IUMzRn0hbBHvHg 提取码：axkz

开始安装:

记得：sudo

chmod u+x acunetix_trial.sh

./acunetix_trial.sh

脚本交互式输入用户信息:

1. 是否同意协议:yes

2. 输入主机名:Taoing

3. 输入管理员邮箱:azxxxxxxxxx.@qq.com

4. 输入密码:Tgxxx./0015

等待.........

成功后会给出地址可以访问看看。

https://Taoing:13443/  # 当然Taoing是你的IP地址  注：你们的不是Taoing哦

建议ifconfig看下虚拟机ip：直接在物理机谷歌浏览器中打开，记得是https

三：破解

下载破解文件: patch_awvs 

将破解文件解压并拷贝到安装目录中

我是直接放在桌面 懒得搞到目录

sudo cp patch_awvs /home/acunetix/.acunetix_trial/v_190325161/scanner/

进入安装目录：cd /home/acunetix/.acunetix_trial/v_190325161/scanner/

加下权限：sudo chmod +x patch_awvs

运行破解程序：sudo ./patch_awvs

显示如上表示成功

检测是否成功：

打开awvs面板 登录以后

点击Administrator->Profile->License",可以看到99999就说明成功激活

关闭自检更新：

登录系统后,左下角Settings->ProductUpgrades,改为"Do not automaticaly check for update[Not Recommanded]"

破解 补丁下载地址：

链接：htts://pan.baidu.com/s/1xvJqt_RVHyb3_17y8XMq_g 提取码：o7cm

