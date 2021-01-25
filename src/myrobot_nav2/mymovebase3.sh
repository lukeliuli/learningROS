
#!/bin/bash

source ~/catkin_ws/devel/setup.bash
{
gnome-terminal -t "start_robot" -x bash -c "roslaunch myrobot_nav2 smartcar_display.rviz.launch;exec bash"
}&

sleep 3s
source ~/catkin_ws/devel/setup.bash
{
gnome-terminal -t "start_move_base" -x bash -c "roslaunch myrobot_nav2 fake_amcl.launch;exec bash"
}&


#sleep 3s
#source ~/catkin_ws/devel/setup.bash

#{
#gnome-terminal -t "echo_cmdvel" -x bash -c "rostopic echo /laser_scan;exec bash"
#}&


#sleep 10s
#source ~/catkin_ws/devel/setup.bash
#{
#gnome-terminal -t "test_cmdvel" -x bash -c "rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped \
#'{ header: { frame_id: "base_link" }, pose: { position: { x: 30.0, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } } }';exec bash"
#}&

