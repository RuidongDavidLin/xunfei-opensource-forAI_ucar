# 赛事功能包是使用说明
####请提前熟悉ROS的基本操作使用；并熟悉ros的安装、工作空间的创建和仿真环境的搭建等内容。
####提前学习迅飞机器人平台的相关教程和资料，参考网址：http://www.iflyros.com/#/courseInfo?id=95
####提前熟悉迅飞机器人平台下载界面的三个文件包及其说明：赛事模版程序、线上竞赛模型文件（训练版本）和线上竞赛模型文件（考核版本）
####提前熟悉古月学院的课程《讯飞创意组机器人导航原理与仿真指南 · 古月》，参考连接：https://class.guyuehome.com/detail/p_6041a333e4b015860af3dba3/6


**1 依赖**

```bash
sudo apt-get install ros-melodic-cartographer*
sudo apt-get install ros-melodic-navigation
sudo apt install ros-melodic-teleop-twist-keyboard
sudo apt install ros-melodic-rqt-graph
sudo apt install ros-melodic-teb-local-planner


**2 解压文件包中的catkin_ws压缩包到主目录下并编译工作空间**
**3 运行模板程序**

在catkin_ws/src/start_game目录下，运行main.py

```bash
cd ~/catkin_ws/src/start_game
python2 main.py
```

脚本运行后，会提醒是否开启录屏，若开启，可以回答“Y”并回车。

接着，脚本所在目录中gazebo_pkg 文件夹下的urdf进行 MD5 校验.

之后，本脚本将自动打开两个标签页，并执行如下命令

```bash
'roscore'
'sleep 5; roslaunch race_navigation teb_demo.launch',
```

具体执行哪些命令可以参照功能讲解修改，这里不再赘述。后两条命令中`sleep 5`的目的是保证其他程序在`roscore`启动完成后才被执行。

全部命令执行完成后，命令行提示“上述命令是否已全部在其他窗口正确执行？ [Y/n]”，这里作出肯定回答

提示“是否开始比赛计时？（务必等待所有软件启动完成后开始！）”，这里继续作出肯定回答，仿真开始，按屏幕上指示进行即可，仿真期间每 30s 打印一次 Topic list。

> * 若打开出现问题可以参考如下操作：
将解压后的文件中的build和devel文件删除，并删除src文件下的CMaKeLists.txt文件，重新设置工作空间和编译文件。







