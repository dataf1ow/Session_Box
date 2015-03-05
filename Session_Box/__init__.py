#__init__.py
from Session_Box import Session_Box


def create_instance(c_instance):
	return Session_Box(c_instance)