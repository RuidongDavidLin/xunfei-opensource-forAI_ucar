2020年3月20日

参赛作品软件环境Ubuntu18.04 ROS Melodic Gazebo

目录结构:

```bash
.
├── .mp4
├── 终点截图
├── md5.md
├── catkin_ws.zip
	├──src  
	    ├── gazebo_pkg
		├── robot_control.launch         #打开gazebo仿真环境
		└── race.launch                  #打开rviz
                └── ...
	    └── open_control_topic
		├── close_vel_publisher.cpp      #控制文件
		└── ...
	    ├── start_game
		└── ...
	    ├── ...
        ├── ...
├── README.MD
```

* `*.mp4`                  提交作品录屏
* `终点截图`               显示红色轮子在停车区域内且无撞墙
* `catkin_ws.zip`          工作空间压缩包
* `src`                    代码文件包
* `README.MD`              本文件

工作空间复现过程：
1.在主目录里新建一个工作空间；
2.将压缩包catkin_ws.zip中的src放入其中；
3.编译该工作空间（我们用的是release(isolated)编译方式）
4.在start_game目录下打开终端，并输入python2 main.py,按照终端提示操作即可

另外，我们于这些操作之前在Ubuntu中安装了如下依赖：
echo "Install the ROS package for art_racecar"
sudo apt-get install ros-melodic-joy -y
sudo apt-get install ros-melodic-move-base -y
sudo apt-get install ros-melodic-mrpt* -y
sudo apt-get install ros-melodic-geographic-msgs -y
sudo apt-get install ros-melodic-map-server -y
sudo apt-get install ros-melodic-gmapping -y
sudo apt-get install ros-melodic-amcl -y
sudo apt-get install ros-melodic-rviz-imu-plugin -y
sudo apt-get install ros-melodic-dwa-local-planner -y
sudo apt-get install ros-melodic-controller-manager -y
sudo apt-get install ros-melodic-gazebo-ros-control -y
sudo apt-get install ros-melodic-effort-controllers -y
sudo apt-get install ros-melodic-joint-state-controller -y
sudo apt-get install ros-melodic-driver-base -y
sudo apt-get install ros-melodic-rtabmap-ros -y
sudo apt-get install ros-melodic-ackermann-msgs -y
sudo apt-get install ros-melodic-teb-local-planner -y
















