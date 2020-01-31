Circle.py Explination 

This code begins with initializing the geometry inputs, then starts the rospy node which twist commands can now be utilized. Then it asks for the user input for angular speed in degrees, angle of turn in degrees and if the user wants the turtlebot to rotate clockwise or counter clocwise. The angles are then converted to radians. An constant linear velocity is given in the x direction to create the circular shape. Once the turtlebot reaches the desired angular distance or returns to 0 degrees, the turtlebot is stopped. 



Square_openloop.py Explination 

This code begins with initializng geometry and math inputs and starting the rospy.init_node to also utilize the twist command. The square is made by giving a x linear velocity when it is commanded to move in the x direction and once it achieves this point with the rate command, it rotates with a given angular velocity. THe XY axis is then "twisted" to allow for the same x linear velocity to remain constant.Thus this is repeated 4 times to create the square. 




Square_closedloop.py Exlplination 

This command was not complete 
