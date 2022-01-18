# 流程指导

## 1.安装该功能包运行需要的控件

driver_base的控件安装
sudo apt-get install ros-melodic-driver-base

controllers控件安装
sudo apt-get install ros-melodic-gazebo-ros-control
sudo apt-get install ros-melodic-effort-controllers
sudo apt-get install ros-melodic-joint-state-controller

planner控件安装
sudo apt-get install ros-melodic-global-planner
sudo apt-get install ros-melodic-teb-local-planner

## 2.将工作空间解压并放置到主目录下

打开工作空间
cd gazebo_test_ws/

删去devel和bulid文件夹

编译工作空间
catkin_make

编译环境
source ./devel/setup.bash


## 3.运行官方脚本

cd src/start_game/
python2 main.py