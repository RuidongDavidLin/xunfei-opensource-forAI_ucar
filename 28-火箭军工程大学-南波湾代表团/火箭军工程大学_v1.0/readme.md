* 把gazebo_test_ws.zip解压缩到/home
* 在gazebo_test_ws目录下，catkin_make编译

  ```bash
  cd ~/gazebo_test_ws
  catkin_make
  ```
(此处若编译不成功，显示可能显示用户关系问题不正确，可在gazebo_test_ws目录下删掉build和devel这两个文件夹，再重新编译）
* 在gazebo_test_ws/src/start_game目录下，运行main.py

```bash
cd ~/gazebo_test_ws/src/start_game
python2 main.py
```
至此即可复现工程
