# Features must include:
# - visual display 
# - layering
# - start, stop, restart, pause, continue playback as a whole and for layer
# - multiple audio inputs
# - adjustable output volume (overall) + layer volume
# - audio bypass (for solo, etc)

#audioloop class contains the loop properties

class audioloop:
    def __init__(self,audio_input, label,length):
        self.audio_input = audio_input
        self.label = label
        self.length = length

#audioaction takes the input from the switches, instantiates a new loop, and does something with it.  Main functionality with the loops are in this class

class audioaction:
    def __init__(self,audioloop,footswitch_input):
        self.audioloop = audioloop
        self.footswitch_input= footswitch_input
        
    def record_layer(audioloop):
        pass
    
    def play(layers):
        pass
    
    def pause(layers):
        pass
    
    #continue can only happen after a pause
        def continue(layers):
            pass
    
    def stop(layers):
        pass
    
    def delete(layers):
        pass
    
    def merge(layers):
        pass

#footswitch class is the interface between the user and the device.  The class itself contains the properties/interactions of the footswitch

class footswitch:
    def __init__(self, label, hold_time,taps):
        self.label = label
        self.hold_time = hold_time
        self.taps = taps

#loopdisplay class holds the message sent to the display.  The input message will depend on the data sent from the footswitches as compared to the loop scenarios overall (how many audio loops, etc).  The output message will need to 'translate' the representation of the scenario based on the type of display used--be it LED's, 7 segment, multi line, etc.

class loopdisplay:
    def __init__(self, input_message, display_type,output_message):
        self.message = message
        self.input_message = input_message
        self.display_type = display_type
        self.output_message = output_message
        
    display_types = ['LED','single 7-segment','multiple 7-segment','multi-line','computer monitor','touchscreen','smartphone','tablet']
    
#audioinout handles/creates the input and output streams on the processing level.  Actual analog handling to be done on the main.py file with the device.  Bypass function is located here for the signal handling; it's initiated by the footswitches dependent on how the programmer would like to implement it on the device.

class audioinout():
    def __init__(self,audio_stream_in,audio_stream_out):
        self.audio_stream_in = audio_stream_in
        self.audio_stream_out = audio_stream_out
    
    def audio_bypass(signal,source,destination):
        pass