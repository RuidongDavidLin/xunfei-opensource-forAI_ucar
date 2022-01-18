# 部署手册
**请您仔细阅读该部署手册，包括4.1注意事项部分！！**
## （首先确认ros安装）
* Ubuntu系统 18.04
* ROS    Melodic
* Gazebo  Gazebo9


**1.1 依赖**

```bash
sudo apt-get install ros-melodic-cartographer*
sudo apt-get install ros-melodic-navigation
sudo apt install ros-melodic-teleop-twist-keyboard
sudo apt install ros-melodic-rqt-graph
```

**1.2 准备工作**

* 把所上传的文件夹中的gazebo_test_ws.zip解压缩到~/home目录下

* 在/home的隐藏文件中找到.bashrc文件，在该文件最后添加一行

  ```bash
  source ~/gazebo_test_ws/devel/setup.bash
  ```
  
* 在gazebo_test_ws目录下，catkin_make编译

  ```bash
  cd ~/gazebo_test_ws
  catkin_make
  ```

* 将 /gazebo_test_ws/start_game/resources/ucar_plane 下的两个
gazebo模型放到 ~/.gazebo/models 下


**2.1 文件结构**

```bash
.
├── gazebo_map	# 建图部分
│   ├── cfg  # 未用到
│   └── launch  # gmapping建图
│   └── map    # 未用到
│   └── CMakeLists.txt
│   └── package.xml
|
├── gazebo_nav	# 导航部分
│   ├── map	# 导航所需地图
|   ├── config	# move_base 配置文件
│   └── scripts
│   │   ├── DWA_path3.py	# 导航有关程序（慢速版）
|   |   ├── DWA_path4.py	# 导航有关程序（不稳版）
|   |   ├── DWA_path5.py	# 导航有关程序（终极版）
│   │   └── DWA_path6.py	# 导航有关程序（调试版）
│   └── launch
│   │   └── navi_demo.launch	# 导航启动文件
│   └── CMakeLists.txt
│   └── package.xml
|
├── start_game	# 脚本部分
│   ├── main.py	# 执行脚本
│   └── initialize.py	# 修改工作空间和urdf路径
│   └──  interactive.py
│   └── ros_module.py
│   └── pose.json	# 导航点
│   └── log.txt
│   └── vital_log.txt
│   └── resources	
│   │   ├── ucar_plane
|
└── gazebo_pkg
```

**2.2 功能讲解**

**2.2.1** SLAM建图

* 启动gmapping的文件在~/gazebo_test_ws/src/gazebo_map/launch中，
同时启动该节点与race.launch，并打开键盘控制，驱动小车走完地图，即可进行slam建图

**2.2.2** 地图位置及命名

* 由gmapping建图的导航所需地图在~/gazebo_test_ws/src/gazebo_nav/map中

**2.2.3 导航**

* 导航目标点在~/gazebo_test_ws/src/start_game/pose.json修改。其中，position下x,y,z为导航目标点位置信息，orientation下x,y,z,w为导航目标点姿态信息。

  ```bash
   {
        "position": 
        {
            "x": -0.0004603767395,
            "y": -5.309980011,
            "z": 0.0
        },
        "orientation": 
        {
            "x": 0.0,
            "y": 0.0,
            "z": 0.999972787533,
            "w": 0.00737727546307
        }
   }
  ```

**3.1 演示部署**

3.1.1不应当使用root执行本脚本

	* 指令前不添加sudo

3.1.2 将python2默认编码修改为utf-8


3.1.3 运行模板程序

* 在gazebo_test_ws/src/start_game目录下，运行main.py

```bash
cd ~/gazebo_test_ws/src/start_game
python2 main.py
```

* 脚本运行后，可以回答“Y”并回车。之后将自动运行导航工程

* 新打开命令终端，利用如下指令开启节点图可视化

```bash
rqt_graph
```

**4.1 注意事项**

* 本录屏使用的追踪脚本为 DWA_path5.py（见navi_demo.launch）。所有版本追踪脚本备注如下：
```bash
  版本             到达终点成功率      平均运行用时
———————————————|——————————————————|————————————————
DWA_path3.py   |      40%         |    30s ~ 32s
DWA_path4.py   |      1%          |    28s ~ 31s
DWA_path5.py   |      30%         |    28s ~ 31s
DWA_path6.py   |      5%          |    28s ~ 31s
```

* 注意部署所需的python版本为python2，编码格式'utf-8'

* 如果运行过程中发现缺少依赖，请安装对应的软件包或功能包

* 如果按上述方案无法部署，请自行新建名为gazebo_test_ws的工作空间，将本目录下的
gazebo_map
gazebo_nav
gazebo_pkg
start_game
复制到新建的gazebo_test_ws下，重新编译再尝试运行


