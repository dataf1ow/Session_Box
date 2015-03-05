#-----------------------------------------------
#                        
#                        
#  Author:                   
#    Evan Bogunia evanbeta@keithmcmillen.com
#                        
#-----------------------------------------------

from __future__ import with_statement

import Live
import time

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent

#define global variables
CHANNEL = 8  #channels are numbered 0 - 15
is_momentary = True

class Session_Box(ControlSurface):
  __module__ = __name__
  __doc__ = "Script that creates  Session Box"
  
  def __init__(self, c_instance):
    ControlSurface.__init__(self, c_instance)
    with self.component_guard():
      self._setup_session_control()
      self.set_highlighting_session_component(self.session)

  def _setup_session_control(self):
    num_tracks = 8 #8 columns (tracks)
    num_scenes = 8 #8 rows (scenes)
    #(num_tracks, num_scenes) a session highlight ("red box") will appear with any two non-zero values
    self.session = SessionComponent(num_tracks,num_scenes)
    self.session.set_offsets(0,0)
  
  
  def disconnect(self):
    #clean things up on disconnect 
    #create entry in log file
    self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()) + "----------Session_Box----------")    
    ControlSurface.disconnect(self)
    return None
