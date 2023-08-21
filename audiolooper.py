# Features must include:
# - visual display 
# - layering
# - start, stop, restart, pause, continue playback as a whole and for layer
# - multiple audio inputs
# - adjustable output volume (overall) + layer volume
# - audio bypass (for solo, etc)


class audioloop:
    def __init__(self,audio_input, footswitch_input, label,length,output_volume,speed):
        self.audio_input = audio_input
        self.footswitch_input = footswitch_input
        self.label = label
        self.length= length
        self.output_volume= output_volume
        self.speed = speed

class footswitch:
    def __init__():
        pass

class loopdisplay():
    def __init__():
        pass

class audioinput():
    def __init__():
        pass