
#!/bin/bash

source ~/catkin_ws/devel/setup.bash
{
gnome-terminal -t "start_robot" -x bash -c "roslaunch myrobot_nav1 smartcar_display.rviz.launch;exec bash"
}&

sleep 20s
source ~/catkin_ws/devel/setup.bash
{
gnome-terminal -t "start_move_base" -x bash -c "roslaunch myrobot_nav1 fake_move_base_blank_map.launch;exec bash"
}&


sleep 3s
source ~/catkin_ws/devel/setup.bash
{
gnome-terminal -t "echo_cmdvel" -x bash -c "rostopic echo /cmd_vel;exec bash"
}&


sleep 10s
source ~/catkin_ws/devel/setup.bash
{
gnome-terminal -t "test_cmdvel" -x bash -c "rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped \
'{ header: { frame_id: "base_link" }, pose: { position: { x: 30.0, y: 0, z: 0 }, orientation: { x: 0, y: 0, z: 0, w: 1 } } }';exec bash"
}&

