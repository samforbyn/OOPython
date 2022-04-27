class DimmerSwitch():
    def __init__(self):
        self.SwitchIsOn = False
        self.brightness = 0
        
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
        