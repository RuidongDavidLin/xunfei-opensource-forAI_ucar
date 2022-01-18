新建工作空间：
gazebo_test_ws

安装的依赖包：
ros-melodic-movebase
ros-melodic-teb-local-planner
ros-melodic-amcl
ros-melodic-costmap

工作空间内包含三个主要功能包
分别为：
gazebo_map
gazebo_nav
gazebo_pkg

已修改main.py中launch_pkg()中启动gazebo仿真并开始导航节点:
roslaunch gazebo_nav navi_demo.launch

已设置initialize.py程序中工作空间路径以及模型文件路径为：
model_path = '~/gazebo_test_ws/src/gazebo_pkg/urdf'
workspace_path = 'source ~/gazebo_test_ws/devel/setup.bash'