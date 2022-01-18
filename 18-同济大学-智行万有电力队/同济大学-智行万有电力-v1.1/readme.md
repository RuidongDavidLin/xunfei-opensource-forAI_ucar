**1.1 依赖**

```bash
sudo apt-get install ros-melodic-cartographer*
sudo apt-get install ros-melodic-navigation
sudo apt install ros-melodic-teleop-twist-keyboard
sudo apt install ros-melodic-rqt-graph
sudo apt-get install ros-melodic-gmapping

rosdep install teb_local_planner

```

**2.1 复现操作**

在gazebo_test_ws/src/start_game目录下，运行main.py

```bash
cd ~/gazebo_test_ws/src/start_game
python2 main.py
```


**3.1 文件结构**

```bash
├── CMakeLists.txt -> /opt/ros/melodic/share/catkin/cmake/toplevel.cmake
├── gazebo_map
│   ├── cfg
│   │   ├── demo.rviz
│   │   └── revo_lds.lua
│   ├── CMakeLists.txt
│   ├── launch
│   │   └── demo_revo_lds.launch
│   ├── map
│   │   ├── mapname.pgm
│   │   └── mapname.yaml
│   └── package.xml
├── gazebo_pkg
│   ├── CMakeLists.txt
│   ├── launch
│   │   └── race.launch
│   ├── meshes
│   │   ├── bot.dae
│   │   └── hokuyo.dae
│   ├── package.xml
│   ├── urdf
│   │   └── waking_robot.xacro
│   └── world
│       └── race_with_cone.world
├── race_navigation
│   ├── CMakeLists.txt
│   ├── config
│   │   ├── dwa
│   │   │   ├── base_global_planner_params.yaml
│   │   │   ├── costmap_common_params.yaml
│   │   │   ├── dwa_local_planner_params.yaml
│   │   │   ├── global_costmap_params.yaml
│   │   │   ├── local_costmap_params.yaml
│   │   │   └── move_base_params.yaml
│   │   ├── lidar.lua
│   │   └── teb
│   │       ├── base_global_planner_params.yaml
│   │       ├── costmap_common_params.yaml
│   │       ├── global_costmap_params.yaml
│   │       ├── local_costmap_params.yaml
│   │       ├── move_base_params.yaml
│   │       └── teb_local_planner_params.yaml
│   ├── launch
│   │   ├── amcl.launch
│   │   ├── cartographer_demo.launch
│   │   ├── dwa_base.launch
│   │   ├── dwa_demo.launch
│   │   ├── gmapping_demo.launch
│   │   ├── gmapping.launch
│   │   ├── teb_base.launch
│   │   └── teb_demo.launch
│   ├── maps
│   │   ├── race.pgm
│   │   └── race.yaml
│   ├── package.xml
│   ├── rviz
│   │   ├── dwa_nav.rviz
│   │   ├── gmapping.rviz
│   │   └── teb_nav.rviz
│   └── scripts
│       └── 111.py
└── start_game
    ├── initialize.py
    ├── initialize.pyc
    ├── interactive.py
    ├── interactive.pyc
    ├── log.txt
    ├── main.py
    ├── pose.json
    ├── resources
    │   └── ucar_plane
    │       ├── end_plane
    │       │   ├── materials
    │       │   │   ├── scripts
    │       │   │   │   └── end_plane.material
    │       │   │   └── textures
    │       │   │       ├── background.png
    │       │   │       ├── end.png
    │       │   │       └── start.png
    │       │   ├── model.config
    │       │   └── model.sdf
    │       └── start_plane
    │           ├── materials
    │           │   ├── scripts
    │           │   │   └── start_plane.material
    │           │   └── textures
    │           │       ├── background.png
    │           │       ├── end.png
    │           │       └── start.png
    │           ├── model.config
    │           └── model.sdf
    ├── ros_module.py
    ├── ros_module.pyc
    └── vital_log.txt

```

