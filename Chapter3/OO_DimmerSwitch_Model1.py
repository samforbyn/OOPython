class DimmerSwitch():
    def __init__(self, label):
        self.SwitchIsOn = False
        self.brightness = 0
        self.label = label 

    def turnOn(self):
        self.SwitchIsOn = True
    
    def turnOff(self):
        self.SwitchIsOn = False
    
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1
        
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1
    
    def show(self):
        print(f'Switch is on?: {self.SwitchIsOn}')
        print(f'Brightness is: {self.brightness}')

# Create first DimmerSwitch, turn it on, and raise the level twice
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Create second DimmerSwitch, turn it on, and raise the level 3 times
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Create third DimmerSwitch, using the default settings
oDimmer3 = DimmerSwitch('Dimmer3')

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()