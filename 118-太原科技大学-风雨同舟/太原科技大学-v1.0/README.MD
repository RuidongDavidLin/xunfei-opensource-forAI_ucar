2020年3月20日

## 说明
* `gazebo_test_ws.zip` 工作空间压缩包
* `md5.md`             md5文件内容
* `仿真录屏.mp4`       工作空间运行仿真的视频录屏视频
* `技术报告.pdf`       线上仿真赛技术报告
* `README.MD`          本文件

## 程序运行步骤：
1. 将gazebo_test_ws.zip解压至home地址下
2. 编译工作空间： 
        cd ~/gazebo_test_ws
        catkin_make
3. 在gazebo_test_ws/src/start_game目录下，运行main.py：
        cd ~/gazebo_test_ws/src/start_game
        python2 main.py

## 程序运行说明
1. 运行程序最低硬件配置： CPU为10代i5，8G内存
2. 本程序在 Linux 平台运行（仅在 Ubuntu 18.04 上进行了测试）
3. 本程序使用普通用户执行本脚本，即不要使用`sudo ./main.py`
4. 本程序使用 Python2 执行（ROS Melodic 不支持 Python 3）
