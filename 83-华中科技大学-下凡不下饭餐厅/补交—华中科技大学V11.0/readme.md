# 工作目录
`~/ ` <br>
<br>

# 按照大学生智能车竞赛教程搭建gazebo环境，创建导航、建图功能，安装赛事模板程序
[链接](http://www.iflyros.com/#/courseInfo?id=95)
<br>
# 安装teb
## 方法一：直接安装teb_local_planner（建议，我们的catkin_ws/src下没有teb_local_planner源码）
`$ sudo apt-get install ros-melodic-teb-local-planner-tutorials` <br>
## 方法二：源码安装teb_local_planner
**安装依赖** <br>
` $  rosdep install teb_local_planner  ` <br>
**源码链接** [teb git源码下载](https://github.com/rst-tu-dortmund/teb_local_planner)<br>
将源码放在**~/catkin_ws/src**下 <br>
**单独编译源码文件** <br>
`$ catkin_make -DCATKIN_WHITELIST_PACKAGES=“源码包名称”`<br>
**查看是否安装成功** <br>
`$ rospack plugins --attrib=plugin nav_core `<br>
如果有teb_local_planner显示，则安装成功 <br>
<br>

#编译
```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
<br>
# 运行赛事计时程序 
```
$ cd ~/catkin_ws/src/start_game 
$  python2 main.py 
```
<br>

#注意
catkin_ws/src下有一些我们之前的学习文件，忘记删掉，表示歉意。直接按照上述流程操作即可。<br>
