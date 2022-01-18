#打开终端 进入功能包

cd catkin_ws


#编译功能包，设置环境变量

catkin_make

source devel/setup.bash

#进入start_game路径下

 cd src/start_game/

#启动脚本(注意将main.py的属性改为可执行)

python2 main.py




