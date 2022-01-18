环境部署与官方教程相同

复现步骤
1.解压工作环境gazebo_test_ws压缩包
2.安装teb-local-planner 插件（已安装可跳过）
 2.1打开终端
 2.2输入  sudo apt-get install ros-melodic-teb-local-planner 
 2.3提示安装成功
3.打开终端运行 赛事脚本

文件结构
.
├── gazebo_map	# 建图部分
│   ├── cfg
│   └── launch
│   └── map
│   └── CMakeLists.txt
│   └── package.xml
├── gazebo_nav	# 导航部分
│   ├── map	# 导航所需地图
│   └── launch
│   │   ├── navi_demo.launch	# 导航所需地图位置在此处修改
│   │   ├── teb_demo.launch	# 调试时快捷启动的launch文件
│   │   └── config	# 参数配置文件
│   └── CMakeLists.txt
│   └── package.xml
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
└── gazebo_pkg

