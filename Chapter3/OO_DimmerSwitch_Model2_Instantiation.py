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

# Create DimmerSwitch objects
oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print()
oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()
oDimmer3 = DimmerSwitch('Dimmer3')
print(type(oDimmer3))
print(oDimmer3)
