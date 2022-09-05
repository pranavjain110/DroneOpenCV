import pygame
import time
def init():

    pygame.init()

    #set size of the pygame window
    win = pygame.display.set_mode((400,400))

def getKey(keyName):
    """ Know if a key is pressed in the pygame window

    Args:
        keyName : The key you want to check

    Returns:
        bool: True if the key is pressed, else False
    """
    
    keyIsPressed = False
    for event in pygame.event.get(): pass
    # Get the state of all the keys on keyboard
    keyInput = pygame.key.get_pressed() 

    # Value of attribute say attribute K_LEFT, K_a from object pygame
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        keyIsPressed = True

    pygame.display.update()

    return keyIsPressed

def main():
    
    if getKey(keyName = "LEFT"): print("Left Key Pressed")
    if getKey(keyName = "RIGHT"): print("RIGHT Key Pressed")
    if getKey(keyName = "UP"): print("UP Key Pressed")
    if getKey(keyName = "DOWN"): print("DOWN Key Pressed")
    if getKey(keyName = "w"): print("w Key Pressed")
    if getKey(keyName = "a"): print("a Key Pressed")
    if getKey(keyName = "s"): print("s Key Pressed")
    if getKey(keyName = "d"): print("d Key Pressed")
    time.sleep(0.1)

# If this file is run directly only then the code below runs
if __name__ == '__main__':
    init()
    while True:
        main()
        # time.sleep()