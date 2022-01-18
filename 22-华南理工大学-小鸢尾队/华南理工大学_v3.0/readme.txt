实验环境配置：
Ubuntu18.04操作系统
ROS Melodic机器人操作系统

安装的程序依赖包：
ros-melodic-desktop-full、ros-melodic-cartographer、ros-melodic-navigation、ros-melodic-teleop-twist-keyboard、ros-melodic-rqt-graph、ros-melodic-teb_local_planner

编译：
更改python2的替换编码

文件结构：
├── gazebo_map	# 建图部分
│     ├── cfg
│     ├── launch
│     ├── map
│     ├── CMakeLists.txt
│     └── package.xml
├── gazebo_nav	# 导航部分
│     ├── map	# 导航所需地图
│     ├── launch
│     │     ├── navi_demo.launch	# 导航所需地图位置在此处修改
│     │     ├── config  	# 参数配置文件
│     │     │     ├── amcl
│     │     │     │     └── amcl_omni.launch
│     │     │     ├── move_base
│     │     │     │     ├── costmap_common_params.yaml
│     │     │     │     ├── global_costmap_params.yaml
│     │     │     │     ├── global_planner_params.yaml
│     │     │     │     ├── local_costmap_params.yaml
│     │     │     │     ├── move_base_params.yaml
│     │     │     │     └── teb_local_planner_params.yaml
│     │     │     ├── rviz
│     │     │     │     └──demo2.rviz
│     ├── CMakeLists.txt
│     └── package.xml
├── start_game	  # 脚本部分
│     ├── main.py	  # 执行脚本
│     ├── initialize.py	# 修改工作空间和urdf路径
│     ├── interactive.py
│     ├── ros_module.py
│     ├── pose.json	  # 导航点
│     ├── log.txt
│     ├── vital_log.txt
│     ├── resources	
│     │     └── ucar_plane
├── gazebo_pkg
│     ├── launch

│     ├── meshes

│     ├── urdf #小车模型参数文件

│     ├── world

│     ├── CMakeLists.txt

│     └── package.xml

└── CMakeLists.txt

复现工作空间的操作：
在gazebo_test_ws/src/start_game目录下，运行main.py