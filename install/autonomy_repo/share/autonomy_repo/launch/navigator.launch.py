
 
#!/usr/bin/env python3

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time")

    declare_use_sim_time = DeclareLaunchArgument(
        "use_sim_time",
        default_value="true",
        description="Use simulation (Gazebo) clock")


    rviz_goal_relay_node = Node(package="asl_tb3_lib",
        executable="rviz_goal_relay.py",
        name="rviz_goal_relay",
        output="screen",
        parameters=[{"output_channel": "/cmd_nav",}])


    state_publisher_node = Node(package="asl_tb3_lib",
       executable="state_publisher.py",name="state_publisher",output="screen",parameters=[{"use_sim_time": use_sim_time}])

    navigator_node = Node(package="autonomy_repo",
      executable="navigator.py",name="navigator",output="screen",parameters=[{"use_sim_time": use_sim_time}] )


    autonomy_share = get_package_share_directory("autonomy_repo")
    default_rviz = os.path.join(autonomy_share, "rviz", "default.rviz")
    asl_tb3_sim_share = get_package_share_directory("asl_tb3_sim")
    rviz_launch_path = os.path.join(asl_tb3_sim_share, "launch", "rviz.launch.py")

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rviz_launch_path),
        launch_arguments={"config": default_rviz,"use_sim_time":use_sim_time,}.items())

        return LaunchDescription(
    [declare_use_sim_time,rviz_goal_relay_node,state_publisher_node,navigator_node,rviz_launch])

