官方赛道文件、小车模型文件gazebo_pkg未变化
官方计时文件start_game文件夹无变化
导航功能包为race_navigation，内含主要文件如下：
launch文件夹：内含导航启动的launch文件teb_demo.launch
config文件夹：内含全局、局部代价地图和teb规划器的参数配置文件
script文件夹：内含自主编写的动态调参程序dynamicconfig.py文件，节点的启动命令
已在main.py文件中修改（其运行需要依赖dynamic_reconfigure包）
map文件夹：内含通过gmapping建图获得的地图文件

复现比赛流程仅需运行python2 main.py指令即可