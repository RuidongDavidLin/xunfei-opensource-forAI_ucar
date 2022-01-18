# readme

## 1. 项目所使用的软硬件平台

平台: Linux-5.4.0-67-generic-x86_64-with-Ubuntu-18.04-bionic ROS-Melodic

CPU: Intel i5-8300H

GPU: NVIDIA GeForce GTX 1050 Ti Mobile

内存: 16GB

## 2. 环境部署

2.1 安装ROS

```shell
sudo apt-get install ros-melodic-desktop-full
```

2.2 将ROS加入环境变量

```shell
#使用bash时
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

#使用zsh时
echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
source ~/.zshrc
```

2.3 安装开发所需依赖

```shell
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

2.4 初始化rosdep

```shell
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```

2.5 安装导航所需依赖以及teb_local_planner

```shell
sudo apt-get install ros-melodic-cartographer*
sudo apt-get install ros-melodic-navigation
sudo apt install ros-melodic-teleop-twist-keyboard
sudo apt install ros-melodic-rqt-graph
sudo apt-get install ros-kinetic-teb-local-planner
```

2.6 将python2默认编码改为utf-8

## 3. 准备工作空间

3.1 将gazebo_test_ws文件夹放在/home/you下，进入gazebo_test_ws文件夹，编译工作空间中的源码包

you替换为自己的用户名

```shell
catkin_make
```

3.2 导入环境变量

```shell
#使用bash时
source devel/setup.bash

#使用zsh时
source devel/setup.zsh
```

3.3 在脚本目录下为脚本添加执行权限

```shell
cd ~/gazebo_test_ws/src/start_game
sudo chown you
chmod u+x *.py
```

## 4. 运行模板程序脚本

```shell
cd ~/gazebo_test_ws/src/start_game
python2 main.py
```

