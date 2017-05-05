#########################################################
# 														#	
# 	  This is main function for this application		#
# 														#
#########################################################

import component

node1 = component.Component("NODE1","sender")
node2 = component.Component("NODE2","receiver")

if __name__ == "__main__":
	print("Running heart of ROS ...")