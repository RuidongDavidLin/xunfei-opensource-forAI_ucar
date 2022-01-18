运行本程序前，请通过以下命令安装对应功能包
sudo apt-get install ros-melodic-costmap-2d
sudo apt-get install ros-melodic-nav-core
sudo apt-get install ros-melodic-navfn
sudo apt-get install ros-melodic-base-local-planner
sudo apt-get install ros-melodic-costmap_converter
sudo apt-get install ros-melodic-mbf_costmap_core
sudo apt-get install ros-melodic-mbf_msgs
sudo apt-get install ros-melodic-libg2o
sudo apt-get install ros-melodic-move-base
sudo apt-get install ros-melodic-map-server
sudo apt-get install ros-melodic-amcl
sudo apt-get install libsuitesparse-dev

用以下命令在根目录下新建gazebo_test_ws文件夹，在gazebo_test_ws文件夹中新建src文件夹，然后编译
mkdir -p ~/gazebo_test_ws/src
cd ~/gazebo_test_ws/
catkin_make

将本功能包/gazebo_test_ws/src/内的六个功能包复制到根目录下工作空间~/gazebo_test_ws/src/下，再编译
cd ~/gazebo_test_ws/
catkin_make

设置环境变量
source ~/gazebo_test_ws/devel/setup.bash

开始运行程序
cd ~/gazebo_test_ws/src/start_game/
python2 main.py





