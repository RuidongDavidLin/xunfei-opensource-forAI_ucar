##############################################
#功能包结构
gazebo_pkg包括小车与赛道的模型文件和配置文件
gazebo_map包括代价地图的配置文件
gazebo_nav包括自主导航配置文件
start_game赛事模板程序

#下载编译
###1.拷贝整个目录到本地
###2.下载依赖
打开终端输入如下指令：
sudo apt-get install ros-melodic-cartographer*
sudo apt-get install ros-melodic-navigation
sudo apt install ros-melodic-teleop-twist-keyboard
sudo apt install ros-melodic-rqt-graph
###3.加执行权限并编译
cd ~/gazebo_test_ws
catkin_make
cd ~/gazebo_test_ws/src/start_game
sudo chown YourAccountName *   #YourAccountName 替换成自己的用户名
chmod u+x *.py

#使用方法：
1.’cd ~/gazebo_test_ws/src/start_game‘
2.’python2 main.py‘（启动赛事模板程序）


