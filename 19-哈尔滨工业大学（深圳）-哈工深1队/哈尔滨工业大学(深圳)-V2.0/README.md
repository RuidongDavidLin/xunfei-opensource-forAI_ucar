# README

- 环境安装

  1. Eigen3库安装

     ```shell
     sudo apt-get install libeigen3 -y
     sudo ln -s /usr/include/eigen3/Eigen /usr/include/Eigen
     ```

  2. ROS相关库安装

     ```shell
     sudo apt-get install ros-melodic-move-base ros-melodic-map-server
     ```

- 编译

  ```shell
  cd path-to-workspace/video_maker
  catkin_make
  ```

- 运行

  ```sh
  roscore
  roslaunch gazebo_pkg race.launch
  roslaunch navigation_pkg AStar_and_amTraj.launch
  ```

