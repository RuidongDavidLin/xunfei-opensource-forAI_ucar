## 部署手册
### 一、环境依赖
- 需要的环境ros-melodic-desktop-full
- 需要的功能包
> ```shell
> sudo apt install ros-melodic-move-base
> sudo apt install ros-melodic-map-server
> sudo apt install ros-melodic-amcl
> sudo apt install ros-melodic-global-planner
> sudo apt install ros-melodic-teb-local-planner
> ```

### 二、部署步骤
1. 首先按照官方的教程，将赛事模型包加载好。
2. 将`gazebo_test_ws.tar.bz2`解压出来
```shell
tar -jxvf gazebo_test_ws.tar.bz2
```
3. 进入`gazebo_test_ws`文件夹，并删除`build`、`devel`、`install`文件夹，然后编译
```shell
cd gazebo_test_ws
rm -r build/ devel/ install/
catkin_make
```
4. 添加环境变量到`bashrc`
5. 运行`main.py`程序
```shell
cd gazebo_test_ws/src/start_game/
python2 main.py
```
