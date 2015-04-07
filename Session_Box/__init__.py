#__init__.py
#Importing our script class
from Session_Box import Session_Box

def create_instance(c_instance):
	#Creates and Returns the Session_Box
	return Session_Box(c_instance)