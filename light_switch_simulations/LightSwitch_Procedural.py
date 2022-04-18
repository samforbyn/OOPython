def turnOn():
    global switchIsOn
    # turn the light on
    switchIsOn = True

def turnOff():
    global switchIsOn
    # turn the light off
    switchIsOn = False

# Main code
switchIsOn = False # a global boolean variable

# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
