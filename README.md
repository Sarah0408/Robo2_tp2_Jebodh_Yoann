## TP2-Partie 2: Navigation

```sh
Author: Khousheeta Jebodh, Yoann Dayvid Lutchmeenaraidoo
```
**Etapes:**
1.On a lance un roscore sur le terminal
2.Ensuite on fait :
 - ssh ubuntu@11.255.255.205 (Pour se connecter au robot)
 - roslaunch turtlebot3_bringup turtlebot3_robot.launch

3.On lance la navigation avec:
 - export TURTLEBOT3_MODEL=waffle.
 - roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=home/info/tb5_map_cleaned_full.yaml 
 (C'est pour afficher l'image qu'on avait map)

4.On a cree un packages avec les depencies :
 - roscpp
 - geometry
 - std
 >catkin_create_pkg move_turtle rospy roscpp geometry_msgs  std_msgs

5.Ensuite on a cherche 3 coordonnees de point :
 - rostopic echo /initialPose
 >En utilisant l'image sur rviz , on a selectionne 3 points sur l'image avec ```2D pose Estimate``` qui fera un cycle 

6.On a cree un noeud goto.py :
 - nano goto.py(pour inserer le code)
 - source devel/setup.bash
 - chmod +x goto.py(pour donnerdroit execution)
 - rosrun move_turtle goto.py
