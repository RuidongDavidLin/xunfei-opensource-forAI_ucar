ʵ�黷�����ã�
Ubuntu18.04����ϵͳ
ROS Melodic�����˲���ϵͳ

��װ�ĳ�����������
ros-melodic-desktop-full��ros-melodic-cartographer��ros-melodic-navigation��ros-melodic-teleop-twist-keyboard��ros-melodic-rqt-graph��ros-melodic-teb_local_planner

���룺
����python2���滻����

�ļ��ṹ��
������ gazebo_map	# ��ͼ����
��     ������ cfg
��     ������ launch
��     ������ map
��     ������ CMakeLists.txt
��     ������ package.xml
������ gazebo_nav	# ��������
��     ������ map	# ���������ͼ
��     ������ launch
��     ��     ������ navi_demo.launch	# ���������ͼλ���ڴ˴��޸�
��     ��     ������ config  	# ���������ļ�
��     ��     ��     ������ amcl
��     ��     ��     ��     ������ amcl_omni.launch
��     ��     ��     ������ move_base
��     ��     ��     ��     ������ costmap_common_params.yaml
��     ��     ��     ��     ������ global_costmap_params.yaml
��     ��     ��     ��     ������ global_planner_params.yaml
��     ��     ��     ��     ������ local_costmap_params.yaml
��     ��     ��     ��     ������ move_base_params.yaml
��     ��     ��     ��     ������ teb_local_planner_params.yaml
��     ��     ��     ������ rviz
��     ��     ��     ��     ������demo2.rviz
��     ������ CMakeLists.txt
��     ������ package.xml
������ start_game	  # �ű�����
��     ������ main.py	  # ִ�нű�
��     ������ initialize.py	# �޸Ĺ����ռ��urdf·��
��     ������ interactive.py
��     ������ ros_module.py
��     ������ pose.json	  # ������
��     ������ log.txt
��     ������ vital_log.txt
��     ������ resources	
��     ��     ������ ucar_plane
������ gazebo_pkg
��     ������ launch

��     ������ meshes

��     ������ urdf #С��ģ�Ͳ����ļ�

��     ������ world

��     ������ CMakeLists.txt

��     ������ package.xml

������ CMakeLists.txt

���ֹ����ռ�Ĳ�����
��gazebo_test_ws/src/start_gameĿ¼�£�����main.py