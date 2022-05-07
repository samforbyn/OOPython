# TV class w/ test code 
class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList =[2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINUMUM = 0 #constant
        self.VOLUME_MAXIMUM = 10 #constant
        self.volume = self.VOLUME_MAXIMUM // 2
    
    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # changing the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False #changing the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINUMUM:
            self.volume -= 1
    
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 # wrap around to first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # wrap around to first channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
    
    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if the newChannel is not in our list of channels, don't do anything
    
    def showInfo(self):
        print("-- TV Status: -- ")
        if self.isOn:
            print("TV is: ON")
            print(f"Channel is: {self.channelList[self.channelIndex]}")
            if self.isMuted: 
                print(f"Volume is: {self.volume} (sound is muted!)")
            else:
                print(f"Volume is: {self.volume}")
        else:
            print("TV is: OFF")