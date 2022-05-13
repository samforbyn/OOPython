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

# Create two DimmerSwitch objects
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer2 = DimmerSwitch('Dimmer2')

# Tell oDimmer1 to raise its level
oDimmer1.raiseLevel()

# Tell oDimmer2 to raise its level
oDimmer2.raiseLevel()

