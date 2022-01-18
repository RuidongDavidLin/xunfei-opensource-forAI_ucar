
关于teb局部规划器：
teb局部规划器可能需要自己安装，命令行（ubuntu18）安装命令如下：sudo apt-get install ros-melodic-teb-local-planner   

安装move_base:
sudo apt-get install ros-melodic-navigation*  

启动方式：
可以直接根据计时程序进行启动：1）打开终端 cd gazebo_test_ws/src/start_game
			    2）输入python2 main.py 




关于功能包介绍：
gazebo_pkg   官方提供包，SLAM建图放在了里面
gazebo_nav    导航功能包，teb 、dwa参数在里面

下面是对于队员的：

建立、保存地图：
1.启动环境和gmapping：roslaunch gazebo_pkg xf_gmapping.launch 
2.启动键盘：rosrun teleop_twist_keyboard teleop_twist_keyboard.py
3.保存地图：rosrun map_server map_saver -f mapname（解释：mapname是你要自己设置的地图名字，此语句保存后，地图保存在home目录下）
4.把保存的地图放到map下，记得修改map的yaml文件，将地图路径名字修改

dwa导航：
1.启动环境和dwa导航：roslaunch gazebo_nav navi_demo.launch 
2.启动导航计时程序:rosrun gazebo_nav move.py

teb导航：
1.启动环境和teb导航：roslaunch gazebo_nav navi_demo_teb.launch 
2.启动导航计时程序:rosrun gazebo_nav move.py

值得注意的是：
move.py这个计时程序的实现方法就是利用程序发布目标点，所以我们不需要再从rviz设置目标点了，打开程序，小车就开始导航了。





