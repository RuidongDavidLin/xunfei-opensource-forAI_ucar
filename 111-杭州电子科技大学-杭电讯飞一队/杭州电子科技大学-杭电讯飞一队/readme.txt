打开文件方式：
注意:视频为vido_last，src的压缩包为src.tar!!!!（另外两个是我之前录错的)
1、可以解压gazebo_test_ws.tar包，此为仿真工作空间。
cd gazebo_test_ws
catkin_make
2、进入start_game文件夹中，用python2 main.py，按照流程打开(因为本人在使用该文件时候，无法通过python脚本打开launch文件，只能单独一个终端打开导航文件。）
3、之后打开另外一个终端，运行
cd gazebo_test_ws
sourse devel/setup.bash
roslaunch keda_mode_start keda_mode_start.launch
会自动打开gazebo以及rviz，等完全打开后，再在python脚本文件终端处发送终点指令，小车便能自动运行
注意：如果无法打开tar包或无法编译gazebo_test_ws这个工作空间，则可以新建一个gazebo_test_ws工作空间，然后把src.tar中的文件放入新建工作空间的src文件中，再编译即可。
编译所需要的包
amcl
teb
gmapping
可通过apt-get install ros-melotic-XXX方式安装
